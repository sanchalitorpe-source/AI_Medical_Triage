from fastapi import FastAPI
from app.env import MedicalTriageEnv
from app.tasks import TASKS
from app.grader import grade
from baseline.run_baseline import run_baseline
from app.models import ResetResponse, TaskResponse, BaselineResponse, GraderResponse

app = FastAPI()
env = MedicalTriageEnv()


@app.get("/", response_model=dict)
def home():
    return {"message": "Medical Triage API is running"}


@app.get("/reset", response_model=ResetResponse)
def reset():
    obs = env.reset()
    return obs


@app.get("/tasks", response_model=TaskResponse)
def get_tasks():
    return {"tasks": TASKS}


@app.get("/baseline", response_model=BaselineResponse)
def baseline():
    score = run_baseline()
    return {"baseline_score": score}


@app.get("/grader", response_model=GraderResponse)
def grader():
    return {
        "message": "Grader active",
        "score_range": "0.0 to 1.0"
    }