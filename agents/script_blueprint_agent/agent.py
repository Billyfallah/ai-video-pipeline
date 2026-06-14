from typing import List
from pydantic import BaseModel
import uuid
import random

class ScriptBlueprintInput(BaseModel):
    trend_id: str
    topic: str
    primary_keyword: str
    target_audience: List[str]

class ScriptBlueprintOutput(BaseModel):
    script_blueprint_id: str
    trend_id: str
    content_angle: str  # Example: educational, entertaining
    content_goal: str  # Example: boost awareness, drive conversions
    narrative_structure: str  # Problem → Solution → Example → CTA
    audience_profile: List[str]
    key_takeaways: List[str]
    emotional_triggers: List[str]
    cta_goal: str

class ScriptBlueprintAgent:
    """Generates a structured blueprint for video script creation."""

    def generate_blueprint(self, input_data: ScriptBlueprintInput) -> ScriptBlueprintOutput:
        """
        Generate a script blueprint based on the input trend and target audience.

        :param input_data: ScriptBlueprintInput containing trend and audience info.
        :return: ScriptBlueprintOutput with structured blueprint details.
        """
        return ScriptBlueprintOutput(
            script_blueprint_id=str(uuid.uuid4()),
            trend_id=input_data.trend_id,
            content_angle=random.choice(["educational", "entertaining", "inspirational"]),
            content_goal=random.choice(["boost awareness", "drive conversions", "engage audience"]),
            narrative_structure="Problem → Solution → Example → CTA",
            audience_profile=input_data.target_audience,
            key_takeaways=[
                f"{input_data.primary_keyword} helps save time.",
                f"{input_data.primary_keyword} improves content quality.",
                "Efficient and cost-effective tools are available."
            ],
            emotional_triggers=["efficiency", "FOMO", "curiosity"],
            cta_goal=f"Encourage adoption of {input_data.primary_keyword}."
        )

# Example usage
if __name__ == "__main__":
    agent = ScriptBlueprintAgent()
    input_data = ScriptBlueprintInput(
        trend_id="yt_ai_video_generator_000",
        topic="AI Video Generator",
        primary_keyword="AI tools",
        target_audience=["content creators", "marketers"]
    )
    blueprint = agent.generate_blueprint(input_data)
    print(blueprint.json(indent=2))