from fastapi import FastAPI
from typing import Dict, Any

from app.env import MedicalTriageEnv
from app.grader import grade
from app.data import TASKS
from app.models import (
    Action, Observation,
    StepResponse, TaskResponse, GraderResponse
)

app = FastAPI(title="Medical Triage OpenEnv", version="1.0.0")

env = MedicalTriageEnv()


@app.get("/")
def root():
    return {"status": "ok", "env": "medical-triage-env"}


@app.post("/reset", response_model=Observation)
def reset() -> Observation:
    obs = env.reset()
    return obs


@app.post("/step", response_model=StepResponse)
def step(action: Action) -> StepResponse:
    obs, reward, done, info = env.step(action)
    return StepResponse(
        observation=obs,
        reward=reward.value,
        done=done,
        info=info
    )


@app.get("/tasks", response_model=TaskResponse)
def get_tasks() -> TaskResponse:
    return TaskResponse(tasks=TASKS)


@app.post("/grader", response_model=GraderResponse)
def grader(action: Action) -> GraderResponse:
    _, reward, _, _ = env.step(action)
    score = grade(reward.value)
    return GraderResponse(score=score, range="0.0 - 1.0")