import pytest
from agents.script_qa_agent.agent import ScriptQAAgent, ScriptQAInput

def test_script_qa_agent():
    """Test the Script QA Agent with valid data."""
    agent = ScriptQAAgent()
    input_data = ScriptQAInput(
        script_id="script_001",
        trend_id="yt_ai_video_generator_000",
        script_blueprint_id="blueprint_001",
        full_script="Detailed script content here."
    )
    
    result = agent.evaluate_script(input_data)
    
    # Assertions
    assert result.script_id == input_data.script_id
    assert 80 <= result.factual_consistency_score <= 95
    assert 75 <= result.engagement_score <= 90
    assert 85 <= result.policy_safety_score <= 100
    assert 0 <= result.overall_qa_score <= 100
    assert result.production_ready in [True, False]
    if not result.production_ready:
        assert "QA score or policy safety too low." in result.blocking_issues

if __name__ == "__main__":
    pytest.main()