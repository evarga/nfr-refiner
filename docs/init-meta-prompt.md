/grill-me

You are an expert Lead Software Engineer helping me refactor a project for a Kaggle hackathon. Please strictly follow the architectural guidelines outlined in the attached @0001-reuse-vs-build.md ADR.

We have just cloned a working template using `agents-cli create sdlc-nfr-refiner -a adk@sdlc-user-story-refiner --yes`. I need you to help me surgically refactor this to become the NFR Refiner. 

Before generating any code, please execute the following steps to prepare:

**Step 1: Knowledge & Context Retrieval**
* Use the **Google Developer Knowledge MCP** tool to retrieve the most up-to-date documentation and best practices for building multi-agent systems using the latest Google Agent Development Kit (ADK). 
* Read the current `agent.py` and any associated schema files in this workspace to understand how the baseline project currently handles routing, state management, and structured output.

**Step 2: Gap Analysis & The Grill**
Compare the existing codebase to the ADR. Identify the exact gaps between the current User Story implementation and our target NFR Planguage implementation. 

Ask me a series of targeted, sequential questions to clarify the implementation details before we write code. Your questions should focus on:
1. How we should adjust the system prompt for the Refiner agent to properly utilize the new `planguage-translator` tool.
2. What specific MCP or API we will use for the web search, and how its output should be appended to the final state.

Do not write or alter any project files until I have answered your questions and explicitly told you to begin the implementation phase.

---
### Provided Context for the Refactoring

**The `planguage-translator` Tool**
The Refiner agent must be equipped with a new, dedicated tool called `planguage-translator`. The final production of the NFR happens entirely through the execution of this tool.