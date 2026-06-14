import pytest
from agents.video_agent.agent import VideoAgent, VideoGenerationTask

def test_video_agent():
    """Test the video generation agent with mock tasks."""
    agent = VideoAgent()
    tasks = [
        VideoGenerationTask(scene_id="scene_001", asset_prompt="AI tool usage montage", asset_style="sleek", duration_seconds=12),
        VideoGenerationTask(scene_id="scene_002", asset_prompt="Key feature animations", asset_style="modern", duration_seconds=8)
    ]
    results = agent.generate_videos(tasks)

    # Assertions
    assert len(results) == len(tasks)
    for result, task in zip(results, tasks):
        assert task.scene_id == result.scene_id
        assert result.file_path.endswith(".mp4")
        assert "scene_" in result.file_path

if __name__ == "__main__":
    pytest.main()