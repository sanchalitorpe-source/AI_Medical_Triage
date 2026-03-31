import random
from typing import Tuple, Dict, Any

from app.models import Observation, Action, Reward
from app.data import CASES


SEVERITY_ORDER = ["low", "medium", "high", "emergency"]


def severity_penalty(pred: str, actual: str) -> float:
    if SEVERITY_ORDER.index(pred) < SEVERITY_ORDER.index(actual):
        return -0.6
    elif SEVERITY_ORDER.index(pred) > SEVERITY_ORDER.index(actual):
        return -0.2
    return 0.0


class MedicalTriageEnv:

    def __init__(self):
        self.current_case = None
        self.step_count = 0
        self.done = False
        self.prev_severity = None

    def reset(self) -> Observation:
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
        if self.done:
            return None, Reward(value=0.0), True, {}

        reward = 0.0
        correct_severity = self.current_case["correct_severity"]
        correct_action = self.current_case["correct_action"]

        if self.step_count == 1:
            if action.severity == correct_severity:
                reward += 0.1
            self.prev_severity = action.severity
            self.step_count += 1

            return Observation(
                symptoms=self.current_case["initial_symptoms"] + self.current_case["followup_info"],
                duration=self.current_case["duration"],
                age=self.current_case["age"],
                history=self.current_case["history"],
                step=self.step_count
            ), Reward(value=reward), False, {}

        else:
            if action.severity == correct_severity:
                reward += 0.4
            else:
                reward += severity_penalty(action.severity, correct_severity)

            if action.action == correct_action:
                reward += 0.4
            else:
                reward -= 0.2

            if (
                self.prev_severity is not None
                and self.prev_severity != correct_severity
                and action.severity == correct_severity
            ):
                reward += 0.2

            self.done = True
            outcome = "stabilized" if reward > 0 else "condition_worsened"
            info = {
                "outcome": outcome,
                "correct_severity": correct_severity,
                "correct_action": correct_action,
            }

            return None, Reward(value=reward), True, info

    def state(self) -> Dict[str, Any]:
        return {
            "step": self.step_count,
            "done": self.done,
            "current_case": self.current_case,
        }