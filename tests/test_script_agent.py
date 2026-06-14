import pytest
from agents.script_agent.agent import ScriptAgent, ScriptInput

def test_script_agent():
    """Test the Script Agent with valid input."""
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

    # Validate output
    assert script.script_blueprint_id == input_data.script_blueprint_id
    assert script.trend_id == input_data.trend_id
    assert len(script.hook) > 0, "Hook should not be empty"
    assert len(script.key_points) > 0, "Key points should not be empty"
    assert script.quality_score >= 0 and script.quality_score <= 100, "Quality score out of range"
    assert script.review_status in ["approved", "review"], "Invalid review status"

if __name__ == "__main__":
    pytest.main()