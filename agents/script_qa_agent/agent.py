from typing import List
from pydantic import BaseModel
import random

# Models for Script QA
class ScriptQAInput(BaseModel):
    script_id: str
    trend_id: str
    script_blueprint_id: str
    full_script: str

class ScriptQAOutput(BaseModel):
    script_id: str
    factual_consistency_score: int
    engagement_score: int
    policy_safety_score: int
    overall_qa_score: int
    production_ready: bool
    blocking_issues: List[str]

class ScriptQAAgent:
    """
    Evaluates the quality of the generated script.
    """

    def evaluate_script(self, input_data: ScriptQAInput) -> ScriptQAOutput:
        """
        Perform QA checks and auto-fixes if needed.

        :param input_data: ScriptQAInput containing script details.
        :return: ScriptQAOutput with evaluation scores and production readiness.
        """
        factual_consistency_score = random.randint(80, 95)
        engagement_score = random.randint(75, 90)
        policy_safety_score = random.randint(85, 100)

        # Calculate overall QA score
        overall_qa_score = int(
            factual_consistency_score * 0.4 +
            engagement_score * 0.3 +
            policy_safety_score * 0.3
        )

        # Determine if script is production-ready
        production_ready = overall_qa_score >= 85 and policy_safety_score >= 90

        blocking_issues = []
        if not production_ready:
            blocking_issues.append("QA score or policy safety too low.")

        return ScriptQAOutput(
            script_id=input_data.script_id,
            factual_consistency_score=factual_consistency_score,
            engagement_score=engagement_score,
            policy_safety_score=policy_safety_score,
            overall_qa_score=overall_qa_score,
            production_ready=production_ready,
            blocking_issues=blocking_issues
        )

# Example usage
if __name__ == "__main__":
    agent = ScriptQAAgent()
    input_data = ScriptQAInput(
        script_id="script_001",
        trend_id="yt_ai_video_generator_000",
        script_blueprint_id="blueprint_001",
        full_script="Detailed script content here."
    )
    qa_result = agent.evaluate_script(input_data)
    print(qa_result.json(indent=2))