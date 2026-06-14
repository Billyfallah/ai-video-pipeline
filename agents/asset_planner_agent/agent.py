from typing import List
from pydantic import BaseModel

# Input and Output Models for Asset Planner
class AssetPlannerInput(BaseModel):
    script_id: str
    production_ready: bool
    scene_breakdown: List[dict]

class AssetTask(BaseModel):
    scene_id: str
    asset_type: str  # image, video_clip, motion_graphics, etc.
    asset_prompt: str
    asset_style: str  # modern, minimalistic, sleek, etc.
    estimated_generation_cost: float

class AssetPlanOutput(BaseModel):
    asset_plan_id: str
    script_id: str
    total_assets: int
    estimated_generation_cost: float
    asset_tasks: List[AssetTask]

class AssetPlannerAgent:
    """
    Generates an asset plan based on the script's scene breakdown.
    """

    def generate_asset_plan(self, input_data: AssetPlannerInput) -> AssetPlanOutput:
        """
        Plan assets required for each scene in the script.

        :param input_data: AssetPlannerInput containing scene breakdown.
        :return: AssetPlanOutput with tasks for asset generation.
        """
        if not input_data.production_ready:
            raise ValueError("Script is not production-ready. Cannot generate asset plan.")

        asset_tasks = []
        total_cost = 0.0
        for scene in input_data.scene_breakdown:
            cost = 5.0  # Placeholder for cost computation logic
            total_cost += cost
            task = AssetTask(
                scene_id=scene["scene_id"],
                asset_type=scene.get("asset_type", "image"),
                asset_prompt=f"Generate visuals for: {scene['scene_goal']}",
                asset_style=scene.get("visual_style", "modern"),
                estimated_generation_cost=cost
            )
            asset_tasks.append(task)

        return AssetPlanOutput(
            asset_plan_id="asset_plan_001",
            script_id=input_data.script_id,
            total_assets=len(asset_tasks),
            estimated_generation_cost=total_cost,
            asset_tasks=asset_tasks
        )

# Example usage
if __name__ == "__main__":
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
    print(asset_plan.json(indent=2))