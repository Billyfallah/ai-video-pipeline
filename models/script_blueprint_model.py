from typing import List
from pydantic import BaseModel

class ScriptBlueprintInput(BaseModel):
    trend_id: str
    topic: str
    primary_keyword: str
    target_audience: List[str]

class ScriptBlueprintOutput(BaseModel):
    script_blueprint_id: str
    trend_id: str
    content_angle: str
    content_goal: str
    narrative_structure: str
    audience_profile: List[str]
    key_takeaways: List[str]
    emotional_triggers: List[str]
    cta_goal: str