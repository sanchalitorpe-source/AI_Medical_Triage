from app.env import MedicalTriageEnv
from app.models import Action

env = MedicalTriageEnv()

def predict(observation: dict) -> dict:
    action = Action(
        severity=observation.get("severity", "low"),
        action=observation.get("action", "self_care")
    )
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict() if obs is not None else None,
        "reward": reward.value,
        "done": done,
        "info": info
    }