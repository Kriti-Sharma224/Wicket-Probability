from pydantic import BaseModel, Field
from typing import List


class BallEvent(BaseModel):
    runs: int = Field(..., ge=0)
    is_wicket: bool
    is_legal: bool


class WicketProbInput(BaseModel):
    events: List[BallEvent]
    match_phase: str
    batter_strike_rate: float = Field(..., gt=0)


class WicketProbOutput(BaseModel):
    balls_bowled: int
    wickets: int
    base_probability: float
    economy: float
    final_probability: float
    interpretation: str