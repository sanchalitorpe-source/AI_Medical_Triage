# inference.py

from app.env import MedicalTriageEnv

env = MedicalTriageEnv()

def predict(observation):
    action, score = env.step(observation)
    return {
        "action": action,
        "score": score
    }