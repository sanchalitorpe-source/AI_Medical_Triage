from pydantic import BaseModel
from typing import List, Literal, Optional, Dict, Any


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


class StepResponse(BaseModel):
    observation: Optional[Observation] = None
    reward: float
    done: bool
    info: Dict[str, Any]


class TaskResponse(BaseModel):
    tasks: List[Dict[str, Any]]


class GraderResponse(BaseModel):
    score: float
    range: str