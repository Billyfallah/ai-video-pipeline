from typing import List
from pydantic import BaseModel
import random

# Input and Output Models for the Image Agent
class ImageGenerationTask(BaseModel):
    scene_id: str
    asset_prompt: str
    asset_style: str

class ImageGenerationResult(BaseModel):
    image_id: str
    scene_id: str
    file_path: str

class ImageAgent:
    """
    Generates images based on the tasks provided by the Asset Planner Agent.
    """

    def generate_images(self, tasks: List[ImageGenerationTask]) -> List[ImageGenerationResult]:
        """
        Generate images for all tasks.

        :param tasks: List of ImageGenerationTask with prompts and styles.
        :return: List of ImageGenerationResult with image file paths.
        """
        results = []
        for task in tasks:
            # Mock image generation logic: Generate a random file path
            file_path = f"/assets/images/{task.scene_id}_{random.randint(1000, 9999)}.png"
            result = ImageGenerationResult(
                image_id=f"image_{random.randint(1000, 9999)}",
                scene_id=task.scene_id,
                file_path=file_path
            )
            results.append(result)
        return results

# Example Usage
if __name__ == "__main__":
    agent = ImageAgent()
    tasks = [
        ImageGenerationTask(scene_id="scene_001", asset_prompt="AI tool usage illustration", asset_style="sleek"),
        ImageGenerationTask(scene_id="scene_002", asset_prompt="Key feature diagram", asset_style="modern")
    ]
    results = agent.generate_images(tasks)
    for res in results:
        print(res.json(indent=2))