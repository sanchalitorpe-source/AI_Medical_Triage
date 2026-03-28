import random
from app.models import Observation, Action, Reward
from app.data import CASES


class MedicalTriageEnv:
    def __init__(self):
        self.current_case = None
        self.step_count = 0
        self.done = False

    def reset(self):
        self.current_case = random.choice(CASES)
        self.step_count = 1
        self.done = False

        return Observation(
            symptoms=self.current_case["initial_symptoms"],
            duration=self.current_case["duration"],
            age=self.current_case["age"],
            history=self.current_case["history"],
            step=self.step_count
        )

    def step(self, action: Action):
        if self.done:
            return None, Reward(value=0), True, {}

        reward = 0
        correct_severity = self.current_case["correct_severity"]
        correct_action = self.current_case["correct_action"]

        if self.step_count == 1:
            if action.severity == correct_severity:
                reward += 0.2

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
                reward -= 0.3

            if action.action == correct_action:
                reward += 0.4
            else:
                reward -= 0.2

            self.done = True

            return None, Reward(value=reward), True, {}