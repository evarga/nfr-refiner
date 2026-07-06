import logging

from google.adk.agents import Agent
from google.adk.planners import BuiltInPlanner
from google.adk.tools import google_search
from google.genai import types

from .config import config
from .prompt import get_refiner_prompt
from .tools.planguage_translator import planguage_translator

logger = logging.getLogger(__name__)

planner = BuiltInPlanner(
    thinking_config=types.ThinkingConfig(
        include_thoughts=False,
        thinking_budget=-1,
    )
)

root_agent = Agent(
    name="refiner",
    model=config.default_llm,
    mode="chat",
    description="Elicits Non-Functional Requirements interactively from the user.",
    instruction=get_refiner_prompt(),
    planner=planner,
    tools=[planguage_translator, google_search],
)

from google.adk.apps import App, ResumabilityConfig

app = App(
    root_agent=root_agent,
    name="nfr_refiner",
    resumability_config=ResumabilityConfig(is_resumable=True),
)
