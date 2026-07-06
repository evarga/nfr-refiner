---
parent: Decisions
nav_order: 1
---

# Reuse vs. Build

## Context and Problem Statement

For the [Kaggle AI Hackathon](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project), we are building an agent that translates vague, free-form product oriented non-functional requirements (NFRs) into strictly quantifiable Planguage specifications based on the [NFRs Guide](https://github.com/evarga/nfrs-guide). The agent should embellish the generated NFR with suggested references, current industry baselines, and advice how to monitor it in production.

## Decision Drivers

* **Ecosystem Integration**: NFRs do not exist in isolation. Our agent is intended to be used as part of a broader software development life cycle (SDLC) workflow, naturally expanding the existing agentic workforce. Moreover, establishing traceability to other artifacts puts NFRs into proper context.
* **Development Velocity**: Maximizing reuse allows us to focus entirely on the new logic rather than boilerplate setup.

## Considered Options

* **Option 1**: Proprietary multi-agent system from scratch.
* **Option 2**: Clone of an existing solution from Google's [Agent Garden](https://console.cloud.google.com/agent-platform/agent-garden).

## Decision Outcome

Chosen option: **Option 2: Clone of an existing solution**.

We have decided to reuse the [User Story Refiner](https://github.com/google/adk-samples/tree/main/python/agents/sdlc-user-story-refiner) project. It handles functional requirements; our NFR Refiner complements it by handling non-functional requirements.

### Architectural Modifications
* **Refiner agent**: Handles the human-in-the-loop elicitation based on the taxonomy from the NFRs Guide. It asks clarifying questions until the required details are known. Once ready, it uses a dedicated `planguage-translator` tool to populate the Planguage template. After the NFR is fully compiled, retrieves additional related data from the web.

## Pros and Cons of the Options

### Option 1: Custom multi-agent system from scratch
* Good, because it provides total control over every line of code and graph edge.
* Bad, because we would develop a toy app fully disconnected from the broader picture. Furthermore, time would be spent on reinventing the wheel instead of enriching the value stream.

### Option 2: Selective clone of an existing solution (Chosen)
* Good, because of reduced cost and risk by building on proven foundation.
* Good, due to massive time savings on infrastructure, database setup, and UI/routing boilerplate by reusing the Google sample.
* Bad, because inheriting AI projects (due to rapid changes in this domain) may bring in obsoleted (deprecated) artifacts, thus accumulate technical debt.