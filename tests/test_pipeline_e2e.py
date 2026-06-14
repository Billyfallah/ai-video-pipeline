import pytest
from agents.script_blueprint_agent.agent import ScriptBlueprintAgent, ScriptBlueprintInput
from agents.script_agent.agent import ScriptAgent, ScriptInput
from agents.script_qa_agent.agent import ScriptQAAgent, ScriptQAInput

def test_pipeline_e2e():
    """Test the full pipeline from Blueprint to Script QA Agent."""

    # Step 1: Script Blueprint Agent
    blueprint_agent = ScriptBlueprintAgent()
    blueprint_input = ScriptBlueprintInput(
        trend_id="yt_ai_video_generator_000",
        topic="AI Video Generator",
        primary_keyword="AI tools",
        target_audience=["content creators", "marketers"]
    )
    blueprint_output = blueprint_agent.generate_blueprint(blueprint_input)

    # Step 2: Script Agent
    script_agent = ScriptAgent()
    script_input = ScriptInput(
        script_blueprint_id=blueprint_output.script_blueprint_id,
        trend_id=blueprint_output.trend_id,
        content_angle=blueprint_output.content_angle,
        narrative_structure=blueprint_output.narrative_structure,
        audience_profile=blueprint_output.audience_profile,
        key_takeaways=blueprint_output.key_takeaways
    )
    script_output = script_agent.generate_script(script_input)

    # Step 3: Script QA Agent
    qa_agent = ScriptQAAgent()
    qa_input = ScriptQAInput(
        script_id=script_output.script_id,
        trend_id=script_output.trend_id,
        script_blueprint_id=script_output.script_blueprint_id,
        full_script=script_output.full_script
    )
    qa_output = qa_agent.evaluate_script(qa_input)

    # Assertions
    assert qa_output.script_id == script_output.script_id
    assert 0 <= qa_output.factual_consistency_score <= 100
    assert 0 <= qa_output.engagement_score <= 100
    assert 0 <= qa_output.policy_safety_score <= 100
    assert 0 <= qa_output.overall_qa_score <= 100
    assert qa_output.production_ready in [True, False]

if __name__ == "__main__":
    pytest.main()