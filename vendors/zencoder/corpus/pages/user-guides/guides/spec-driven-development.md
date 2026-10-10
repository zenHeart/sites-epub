> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Spec-Driven Development with Zenflow: Why It Works

This guide covers how Spec-Driven Development (SDD) works in Zenflow, including the core philosophy, workflow stages, and when to use it versus a "Quick Change" approach.\
**The Problem with Prompt-and-Pray**

The typical approach — type a prompt, get code, fix what's wrong, repeat — works for simple tasks. For anything complex, it falls apart.

**Typical AI-Assisted Development Iterations:**

* **Round 1:** "Add a notification system."
  * *AI builds toast notifications. Not what you meant.*
* **Round 2:** "No, backend notifications for orders."
  * *AI creates a basic email service. Missing pieces.*
* **Round 3:** "Also SMS, and user preferences."
  * *AI bolts on features to code that wasn't designed for them.*

Each iteration loses context. The final code is a patchwork of fixes, not a coherent design. This is **prompt-and-pray**: throw requirements at the AI incrementally, hope it figures out what you mean, and clean up the mess afterward.\
\
**Why Specifications Work**

SDD is a methodology where you define the **complete requirements and technical specifications upfront**—then let the agent execute against that specification.

A specification answers key questions before coding starts:

* Who needs this and why?
* What does success look like (quantifiable)?
* What's in scope—and what's explicitly out?
* How should this integrate with existing systems?
* What constraints must be respected?

When an AI has this information upfront, there's nothing to interpret—just execute.

* **Without a spec:** The AI guesses based on training data patterns. Every missing piece of context is a potential wrong assumption.
* **With a spec:** The AI knows exactly what to build, which services to use, what constraints to respect, and what success means. **No guessing.**

The core insight is that AI agents are **literal executors, not intuitive collaborators**. Specifications remove ambiguity. The agent becomes an executor, not an interpreter.\
**How Zenflow Implements SDD (The Full SDD Workflow)**

Zenflow formalizes SDD into a four-stage process, producing three key artifacts:

| **Artifact** | **Description** |
| :- | :- |
| [**requirements.md**](http://requirements.md) | Product Requirements Document (PRD). Captures user stories, success criteria, and explicit out-of-scope items. |
| [**spec.md**](http://spec.md) | Technical specification. Details architecture, database schemas, and API contracts. |
| [**plan.md**](http://plan.md) | Implementation plan. Breaks the work into ordered, verifiable steps. |

**The Four Stages:**

1. **Stage 1: Requirements Gathering**
   * The agent prompts you with questions (e.g., "What's explicitly out of scope?").
   * Your responses are compiled into [requirements.md](http://requirements.md). **You review and edit this file before approval.**
2. **Stage 2: Technical Specification**
   * The agent analyzes your codebase and produces [spec.md](http://spec.md).
   * This is the **cheapest place to catch design mistakes**—review the proposed database changes and architecture before any code is written.
3. **Stage 3: Implementation Planning**
   * The agent breaks the spec into [plan.md](http://plan.md) with ordered, dependent steps (e.g., database migrations before API endpoints).
   * **You can reorder, add, or remove steps** before implementation begins.
4. **Stage 4: Implementation with Verification**
   * The agent implements each step in order.
   * After each step, an **AI verifier reviews the code diff** against the spec, flagging issues before proceeding.
   * You can intervene, approve, or request changes at any point.

**When to Use SDD vs. Quick Change**

**Use the Full SDD Workflow when:**

* The feature touches **5+ files or multiple services**.
* You need **stakeholder review** before implementation.
* There are **compliance or audit requirements**.
* Work spans **multiple days**.
* Breaking changes require **migration planning**.

**Use Quick Change instead when:**

* The task fits in **one sentence with no ambiguity**.
* Expected implementation time is **under 10 minutes**.
* **No architectural decisions** are needed.

**Configuration**

Agent presets control SDD behavior. In **Settings → Saved presets**, you can configure:

* Model selection (e.g., Claude, GPT-4, Gemini)
* Custom prompt overrides for each stage

Spec-Driven Development in Zenflow uses structured artifacts ([requirements.md](http://requirements.md), [spec.md](http://spec.md), [plan.md](http://plan.md)) to give AI agents complete context before implementation. The four-stage workflow—requirements, specification, planning, implementation—provides checkpoints for review and verification.

For complex features, this approach produces more predictable results than iterative prompting, with documentation as a byproduct.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.