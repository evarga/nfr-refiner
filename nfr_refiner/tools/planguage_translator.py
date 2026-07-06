import logging
from typing import Literal

from google.adk.tools import ToolContext
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class PlanguageRequirement(BaseModel):
    tag: str = Field(description="Structured name of the NFR")
    gist: str = Field(
        description="Brief description of the NFR. This MUST be a proper, concise summary capturing the true essence of the requirement."
    )
    ambition: str = Field(
        description="Short briefing about the rationale behind the NFR"
    )
    scale: str = Field(description="Unit of measure with context")
    meter: str = Field(description="Measurement method")
    baseline: str = Field(
        description="The current level relative to the NFR in question"
    )
    fail: str = Field(description="Point where the QA test fails")
    goal: str = Field(
        description="Point where we fully approve the test in a sense of having achieved our objective"
    )
    stretch: str = Field(description="Limit above which ROI is negligible")


async def planguage_translator(
    category: Literal[
        "Usability",
        "Reliability",
        "Performance",
        "Supportability",
        "Security",
        "Maintainability",
    ],
    subcategory: str,
    gist: str,
    ambition: str,
    scale: str,
    meter: str,
    baseline: str,
    fail: str,
    goal: str,
    stretch: str,
    tool_context: ToolContext,
) -> dict:
    """
    Translates the gathered NFR details into the strict Planguage format.
    Use this skill ONLY once ALL required fields of the NFR have been fully elicited and confirmed with the user.

    Instructions:
    - You must populate all the Planguage fields accurately based on the conversation history.
    - Carefully formulate the `gist` to be a highly accurate and professional summary of the requirement.

    Args:
        category: The top-level FURPS+ category.
        subcategory: The specific sub-level FURPS+ category.
        gist: Brief description of the NFR. Must be a proper, concise summary.
        ambition: Short briefing about the rationale behind the NFR.
        scale: Unit of measure with context.
        meter: Measurement method.
        baseline: The current level relative to the NFR in question.
        fail: Point where the QA test fails.
        goal: Point where we fully approve the test.
        stretch: Limit above which ROI is negligible.
    """
    req = PlanguageRequirement(
        tag=f"{category}.{subcategory}",
        gist=gist,
        ambition=ambition,
        scale=scale,
        meter=meter,
        baseline=baseline,
        fail=fail,
        goal=goal,
        stretch=stretch,
    )

    logger.info(f"NFR compiled successfully: {req.tag}")
    return {"status": "success", "compiled_nfr": req.model_dump()}
