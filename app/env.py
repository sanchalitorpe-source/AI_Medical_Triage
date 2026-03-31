import random
from typing import Tuple, Dict, Any

from app.models import Observation, Action, Reward
from app.data import CASES


SEVERITY_ORDER = ["low", "medium", "high", "emergency"]


def severity_penalty(pred: str, actual: str) -> float:
    """
    Penalize incorrect severity predictions.
    Underestimation is heavily penalized.
    """
    if SEVERITY_ORDER.index(pred) < SEVERITY_ORDER.index(actual):
        return -0.6  # dangerous underestimation
    elif SEVERITY_ORDER.index(pred) > SEVERITY_ORDER.index(actual):
        return -0.2  # safer but unnecessary escalation
    return 0.0


class MedicalTriageEnv:
    """
    Clinical Triage Decision Environment (Deterministic & Safe)

    Multi-step RL environment:
    Step 1 → initial triage
    Step 2 → updated info → final decision
    """

    def __init__(self):
        self.current_case = None
        self.step_count = 0
        self.done = False
        self.prev_severity = None

    def reset(self) -> Observation:
        """
        Start a new episode by sampling a random case.
        """
        self.current_case = random.choice(CASES)
        self.step_count = 1
        self.done = False
        self.prev_severity = None

        return Observation(
            symptoms=self.current_case["initial_symptoms"],
            duration=self.current_case["duration"],
            age=self.current_case["age"],
            history=self.current_case["history"],
            step=self.step_count
        )

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict[str, Any]]:
        """
        Execute one step in the environment.
        """

        if self.done:
            return None, Reward(value=0.0), True, {}

        reward = 0.0
        correct_severity = self.current_case["correct_severity"]
        correct_action = self.current_case["correct_action"]

        # -------------------------
        # STEP 1: Initial decision
        # -------------------------
        if self.step_count == 1:
            # Small reward for early correct guess
            if action.severity == correct_severity:
                reward += 0.1

            # Store previous decision for consistency check
            self.prev_severity = action.severity

            self.step_count += 1

            return Observation(
                symptoms=self.current_case["initial_symptoms"]
                + self.current_case["followup_info"],
                duration=self.current_case["duration"],
                age=self.current_case["age"],
                history=self.current_case["history"],
                step=self.step_count
            ), Reward(value=reward), False, {}

        # -------------------------
        # STEP 2: Final decision
        # -------------------------
        else:
            # Severity evaluation
            if action.severity == correct_severity:
                reward += 0.4
            else:
                reward += severity_penalty(action.severity, correct_severity)

            # Action evaluation
            if action.action == correct_action:
                reward += 0.4
            else:
                reward -= 0.2

            # Consistency / improvement bonus
            if (
                self.prev_severity is not None
                and self.prev_severity != correct_severity
                and action.severity == correct_severity
            ):
                reward += 0.2

            self.done = True

            # Simulated patient outcome
            outcome = "stabilized" if reward > 0 else "condition_worsened"

            info = {
                "outcome": outcome,
                "correct_severity": correct_severity,
                "correct_action": correct_action,
            }

            return None, Reward(value=reward), True, info

    def state(self) -> Dict[str, Any]:
        """
        Return internal state (for debugging / OpenEnv compliance).
        """
        return {
            "step": self.step_count,
            "done": self.done,
            "current_case": self.current_case,
        }