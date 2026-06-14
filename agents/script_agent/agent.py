from typing import List
from pydantic import BaseModel
import uuid
import random

class ScriptInput(BaseModel):
    script_blueprint_id: str
    trend_id: str
    content_angle: str
    narrative_structure: str
    audience_profile: List[str]
    key_takeaways: List[str]

class ScriptOutput(BaseModel):
    script_id: str
    trend_id: str
    script_blueprint_id: str
    hook: str
    outline: str
    key_points: List[str]
    full_script: str
    quality_score: int
    review_status: str

class ScriptAgent:
    """
    Generates a script based on blueprint and trend.
    """

    def generate_script(self, input_data: ScriptInput) -> ScriptOutput:
        """
        Generate the script.

        :param input_data: Blueprint input containing all required data.
        :return: ScriptOutput containing full script details.
        """
        hook = f"Discover the power of {input_data.content_angle} storytelling!"
        outline = "Intro → Features → Benefits → Call to Action"
        key_points = input_data.key_takeaways + ["Engage your audience effectively.", "Drive your message home."]
        full_script = f"Title: {input_data.content_angle} Storytelling\nKey Points: {', '.join(key_points)}\nEncourage action today!"

        quality_score = random.randint(80, 95)
        review_status = "approved" if quality_score >= 85 else "review"

        return ScriptOutput(
            script_id=str(uuid.uuid4()),
            trend_id=input_data.trend_id,
            script_blueprint_id=input_data.script_blueprint_id,
            hook=hook,
            outline=outline,
            key_points=key_points,
            full_script=full_script,
            quality_score=quality_score,
            review_status=review_status
        )

# Example usage
if __name__ == "__main__":
    agent = ScriptAgent()
    input_data = ScriptInput(
        script_blueprint_id="blueprint_001",
        trend_id="yt_ai_video_generator_000",
        content_angle="educational",
        narrative_structure="Problem → Solution → Example → CTA",
        audience_profile=["content creators", "marketers"],
        key_takeaways=["AI tools save time for creators.", "Boost content quality."]
    )
    script = agent.generate_script(input_data)
    print(script.json(indent=2))