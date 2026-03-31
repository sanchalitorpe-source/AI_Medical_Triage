from pydantic import BaseModel
from typing import List, Literal, Optional, Dict, Any


# -------------------------
# Core Models
# -------------------------
class Observation(BaseModel):
    symptoms: List[str]
    duration: str
    age: int
    history: List[str]
    step: int


class Action(BaseModel):
    severity: Literal["low", "medium", "high", "emergency"]
    action: Literal["self_care", "visit_doctor", "urgent_care", "go_to_er"]


class Reward(BaseModel):
    value: float


# -------------------------
# API Response Models
# -------------------------
class ResetResponse(BaseModel):
    observation: Observation


class StepResponse(BaseModel):
    observation: Optional[Observation]
    reward: float
    done: bool
    info: Dict[str, Any]


class TaskResponse(BaseModel):
    tasks: List[Dict[str, Any]]


class BaselineResponse(BaseModel):
    baseline_score: float


class GraderResponse(BaseModel):
    score: float
    range: str