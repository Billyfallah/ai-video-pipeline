import pytest
from agents.image_agent.agent import ImageAgent, ImageGenerationTask

def test_image_agent():
    """Test the image generation agent with mock tasks."""
    agent = ImageAgent()

    tasks = [
        ImageGenerationTask(scene_id="scene_001", asset_prompt="AI tool usage illustration", asset_style="sleek"),
        ImageGenerationTask(scene_id="scene_002", asset_prompt="Key feature diagram", asset_style="modern")
    ]

    results = agent.generate_images(tasks)

    # Assertions
    assert len(results) == len(tasks)
    for result, task in zip(results, tasks):
        assert task.scene_id == result.scene_id
        assert result.file_path.endswith(".png")
        assert "scene_" in result.file_path

if __name__ == "__main__":
    pytest.main()