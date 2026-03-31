from app.env import MedicalTriageEnv
from app.models import Action
from app.grader import grade


def simple_agent(obs):
    symptoms = [s.lower() for s in obs.symptoms]

    # -------------------------
    # STEP-AWARE LOGIC
    # -------------------------
    if obs.step == 1:
        # Conservative initial guess
        if "chest pain" in symptoms:
            return Action(severity="high", action="urgent_care")

        if "fever" in symptoms:
            return Action(severity="low", action="self_care")

        return Action(severity="medium", action="visit_doctor")

    else:
        # Final decision after more info

        if "chest pain" in symptoms and "shortness of breath" in symptoms:
            return Action(severity="emergency", action="go_to_er")

        if "blurred vision" in symptoms or "loss of vision" in symptoms:
            return Action(severity="high", action="urgent_care")

        if "vomiting" in symptoms and "dehydration" in symptoms:
            return Action(severity="medium", action="visit_doctor")

        if "fever" in symptoms or "minor cut" in symptoms:
            return Action(severity="low", action="self_care")

        return Action(severity="medium", action="visit_doctor")


def run_episode(env):
    obs = env.reset()
    total_reward = 0.0
    done = False

    while not done:
        action = simple_agent(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward.value

    return grade(total_reward)


def run_baseline():
    env = MedicalTriageEnv()

    # Run multiple episodes for stability
    scores = [run_episode(env) for _ in range(10)]

    return round(sum(scores) / len(scores), 3)