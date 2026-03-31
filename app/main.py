from fastapi import FastAPI, Body

from app.env import MedicalTriageEnv
from app.tasks import TASKS
from app.grader import grade
from baseline.run_baseline import run_baseline
from app.models import Action

app = FastAPI(
    title="Clinical Triage OpenEnv",
    description="Deterministic RL environment for medical triage decision-making",
    version="1.0"
)

env = MedicalTriageEnv()


# -------------------------
# Root Endpoint
# -------------------------
@app.get("/")
def home():
    return {"message": "Medical Triage API is running"}


# -------------------------
# Health Check
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Reset Environment
# -------------------------
@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()   # IMPORTANT


# -------------------------
# Step Endpoint (REQUIRED)
# -------------------------
@app.post("/step")
def step(action: Action = Body(...)):
    obs, reward, done, info = env.step(action)

    if obs:
        return {
            "symptoms": obs.symptoms,
            "duration": obs.duration,
            "age": obs.age,
            "history": obs.history,
            "step": obs.step,
            "reward": reward.value,
            "done": done
        }
    else:
        return {
            "symptoms": [],
            "duration": "",
            "age": 0,
            "history": [],
            "step": 0,
            "reward": reward.value,
            "done": done
        }


# -------------------------
# Tasks Endpoint
# -------------------------
@app.get("/tasks")
def get_tasks():
    return {"tasks": TASKS}


# -------------------------
# Baseline Endpoint
# -------------------------
@app.get("/baseline")
def baseline():
    score = run_baseline()
    return {"baseline_score": score}


# -------------------------
# Grader Endpoint
# -------------------------
@app.post("/grader")
def grader_endpoint(total_reward: float):
    score = grade(total_reward)

    return {
        "score": score,
        "range": "0.0 to 1.0"
    }