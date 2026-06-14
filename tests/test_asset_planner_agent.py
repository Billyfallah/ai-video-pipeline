import pytest
from agents.asset_planner_agent.agent import AssetPlannerAgent, AssetPlannerInput

def test_asset_planner_agent():
    """Test the Asset Planner Agent with valid input."""
    agent = AssetPlannerAgent()

    input_data = AssetPlannerInput(
        script_id="script_001",
        production_ready=True,
        scene_breakdown=[
            {"scene_id": "scene_001", "scene_goal": "Introduce AI tools", "asset_type": "video_clip", "visual_style": "sleek"},
            {"scene_id": "scene_002", "scene_goal": "Highlight key features", "asset_type": "image", "visual_style": "minimalistic"}
        ]
    )

    asset_plan = agent.generate_asset_plan(input_data)

    # Assertions
    assert asset_plan.script_id == input_data.script_id
    assert asset_plan.asset_plan_id is not None
    assert asset_plan.total_assets == len(input_data.scene_breakdown)
    assert asset_plan.estimated_generation_cost > 0
    assert len(asset_plan.asset_tasks) > 0

if __name__ == "__main__":
    pytest.main()