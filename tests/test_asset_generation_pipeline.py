import pytest
from agents.asset_planner_agent.agent import AssetPlannerAgent, AssetPlannerInput
from agents.image_agent.agent import ImageAgent, ImageGenerationTask
from agents.video_agent.agent import VideoAgent, VideoGenerationTask

def test_asset_generation_pipeline():
    """Test the pipeline from Asset Planner to Image and Video Agents."""

    # Step 1: Asset Planner
    asset_planner_agent = AssetPlannerAgent()
    asset_planner_input = AssetPlannerInput(
        script_id="script_001",
        production_ready=True,
        scene_breakdown=[
            {"scene_id": "scene_001", "scene_goal": "Introduce AI tools", "asset_type": "video_clip", "visual_style": "sleek"},
            {"scene_id": "scene_002", "scene_goal": "Highlight features", "asset_type": "image", "visual_style": "modern"}
        ]
    )
    asset_plan = asset_planner_agent.generate_asset_plan(asset_planner_input)

    # Step 2: Image Agent
    image_agent = ImageAgent()
    image_tasks = [
        ImageGenerationTask(scene_id=task.scene_id, asset_prompt=task.asset_prompt, asset_style=task.asset_style)
        for task in asset_plan.asset_tasks if task.asset_type == "image"
    ]
    image_results = image_agent.generate_images(image_tasks)

    # Step 3: Video Agent
    video_agent = VideoAgent()
    video_tasks = [
        VideoGenerationTask(scene_id=task.scene_id, asset_prompt=task.asset_prompt, asset_style=task.asset_style, duration_seconds=10)
        for task in asset_plan.asset_tasks if task.asset_type == "video_clip"
    ]
    video_results = video_agent.generate_videos(video_tasks)

    # Assertions
    assert len(image_results) == 1
    assert len(video_results) == 1

    for image in image_results:
        assert image.file_path.endswith(".png")

    for video in video_results:
        assert video.file_path.endswith(".mp4")

if __name__ == "__main__":
    pytest.main()