from fastapi import FastAPI
from app.env import MedicalTriageEnv
from app.tasks import TASKS
from app.grader import grade
from baseline.run_baseline import run_baseline
from app.models import ResetResponse, TaskResponse, BaselineResponse, GraderResponse

app = FastAPI(title="Medical Triage OpenEnv API")

env = MedicalTriageEnv()


# ✅ Home (for browser)
@app.get("/")
def home():
    return {
        "message": "Medical Triage API is running",
        "docs": "/docs",
        "endpoints": ["/reset", "/step", "/tasks", "/baseline", "/grader"]
    }


# ✅ REQUIRED: POST reset (OpenEnv expects this)
@app.post("/reset", response_model=ResetResponse)
def reset():
    obs = env.reset()
    return obs


# (optional GET for manual testing)
@app.get("/reset")
def reset_get():
    return env.reset()


# ✅ REQUIRED: step() endpoint (IMPORTANT for OpenEnv)
@app.post("/step")
def step(action: dict):
    observation, reward, done, info = env.step(action)
    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }


# ✅ Tasks endpoint
@app.get("/tasks", response_model=TaskResponse)
def get_tasks():
    return {"tasks": TASKS}


# ✅ Baseline endpoint
@app.get("/baseline", response_model=BaselineResponse)
def baseline():
    score = run_baseline()
    return {"baseline_score": score}


# ✅ Grader endpoint
@app.get("/grader", response_model=GraderResponse)
def grader():
    return {
        "message": "Grader active",
        "score_range": "0.0 to 1.0"
    }