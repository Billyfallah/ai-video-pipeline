import pytest
from agents.script_blueprint_agent.agent import ScriptBlueprintAgent, ScriptBlueprintInput

def test_script_blueprint_agent():
    """Test the Script Blueprint Agent with valid input."""
    agent = ScriptBlueprintAgent()
    input_data = ScriptBlueprintInput(
        trend_id="yt_ai_video_generator_000",
        topic="AI Video Generator",
        primary_keyword="AI tools",
        target_audience=["content creators", "marketers"]
    )

    blueprint = agent.generate_blueprint(input_data)

    # Validate output
    assert blueprint.trend_id == input_data.trend_id
    assert blueprint.script_blueprint_id is not None
    assert blueprint.content_angle in ["educational", "entertaining", "inspirational"]
    assert blueprint.content_goal in ["boost awareness", "drive conversions", "engage audience"]
    assert blueprint.narrative_structure == "Problem → Solution → Example → CTA"
    assert len(blueprint.key_takeaways) > 0
    assert "efficiency" in blueprint.emotional_triggers

if __name__ == "__main__":
    pytest.main()