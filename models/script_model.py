from typing import List
from pydantic import BaseModel

class ScriptInput(BaseModel):
    script_blueprint_id: str
    trend_id: str

class ScriptOutput(BaseModel):
    script_id: str
    script_blueprint_id: str
    hook: str
    outline: str
    key_points: List[str]
    full_script: str
    quality_score: int