from pydantic import BaseModel
from typing import List


class Observation(BaseModel):
    symptoms: List[str]
    duration: str
    age: int
    history: List[str]
    step: int


class Action(BaseModel):
    severity: str
    action: str


class Reward(BaseModel):
    value: float


class ResetResponse(BaseModel):
    symptoms: List[str]
    duration: str
    age: int
    history: List[str]
    step: int


class TaskResponse(BaseModel):
    tasks: list


class BaselineResponse(BaseModel):
    baseline_score: float


class GraderResponse(BaseModel):
    message: str
    score_range: str