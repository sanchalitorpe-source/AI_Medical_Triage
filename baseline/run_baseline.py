from app.env import MedicalTriageEnv
from app.models import Action
from app.grader import grade


def simple_agent(obs):
    symptoms = [s.lower() for s in obs.symptoms]

    if "chest pain" in symptoms and "shortness of breath" in symptoms:
        return Action(severity="emergency", action="go_to_er")

    if "blurred vision" in symptoms:
        return Action(severity="high", action="urgent_care")

    if "vomiting" in symptoms:
        return Action(severity="medium", action="doctor")

    if "fever" in symptoms or "minor cut" in symptoms:
        return Action(severity="low", action="self_care")

    return Action(severity="medium", action="doctor")


def run_episode(env):
    obs = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = simple_agent(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward.value

    return grade(total_reward)


def run_baseline():
    env = MedicalTriageEnv()
    scores = [run_episode(env) for _ in range(5)]
    return round(sum(scores) / len(scores), 3)