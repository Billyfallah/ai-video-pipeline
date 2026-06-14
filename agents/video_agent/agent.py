from typing import List
from pydantic import BaseModel
import random

# Input and Output Models for the Video Agent
class VideoGenerationTask(BaseModel):
    scene_id: str
    asset_prompt: str
    asset_style: str
    duration_seconds: int

class VideoGenerationResult(BaseModel):
    video_id: str
    scene_id: str
    file_path: str

class VideoAgent:
    """
    Generates video clips based on tasks provided by the Asset Planner Agent.
    """

    def generate_videos(self, tasks: List[VideoGenerationTask]) -> List[VideoGenerationResult]:
        """
        Generate video clips for all tasks.

        :param tasks: List of VideoGenerationTask with prompts, styles, and durations.
        :return: List of VideoGenerationResult with video file paths.
        """
        results = []
        for task in tasks:
            # Mock video generation logic: Generate a random file path
            file_path = f"/assets/videos/{task.scene_id}_{random.randint(1000, 9999)}.mp4"
            result = VideoGenerationResult(
                video_id=f"video_{random.randint(1000, 9999)}",
                scene_id=task.scene_id,
                file_path=file_path
            )
            results.append(result)
        return results

# Example usage
if __name__ == "__main__":
    agent = VideoAgent()
    tasks = [
        VideoGenerationTask(scene_id="scene_001", asset_prompt="AI tool usage montage", asset_style="sleek", duration_seconds=12),
        VideoGenerationTask(scene_id="scene_002", asset_prompt="Key feature animations", asset_style="modern", duration_seconds=8)
    ]
    results = agent.generate_videos(tasks)
    for res in results:
        print(res.json(indent=2))