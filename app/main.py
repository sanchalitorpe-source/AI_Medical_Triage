from fastapi import FastAPI
from typing import Dict, Any

from app.env import MedicalTriageEnv
from app.tasks import TASKS
from app.grader import grade
from baseline.run_baseline import run_baseline
from app.models import (
    ResetResponse,
    TaskResponse,
    BaselineResponse,
    GraderResponse,
    Action,
)

app = FastAPI(
    title="Clinical Triage OpenEnv",
    description="Deterministic RL environment for medical triage decision-making",
    version="1.0"
)

env = MedicalTriageEnv()


# -------------------------
# Root Endpoint
# -------------------------
@app.get("/", response_model=dict)
def home():
    return {"message": "Medical Triage API is running"}


# -------------------------
# Health Check (Optional but useful)
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Reset Environment
# -------------------------
@app.get("/reset", response_model=ResetResponse)
def reset():
    obs = env.reset()
    return obs


# -------------------------
# Step Endpoint (REQUIRED)
# -------------------------
from fastapi import Body
from app.models import Action

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
@app.get("/tasks", response_model=TaskResponse)
def get_tasks():
    return {"tasks": TASKS}


# -------------------------
# Baseline Endpoint
# -------------------------
@app.get("/baseline", response_model=BaselineResponse)
def baseline():
    score = run_baseline()
    return {"baseline_score": score}


# -------------------------
# Grader Endpoint
# -------------------------
@app.post("/grader", response_model=GraderResponse)
def grader_endpoint(total_reward: float):
    score = grade(total_reward)

    return {
        "score": score,
        "range": "0.0 to 1.0"
    }