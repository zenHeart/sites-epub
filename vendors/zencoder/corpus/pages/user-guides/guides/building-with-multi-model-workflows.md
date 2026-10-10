> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Building an Application with Multi-Model Workflows

> A step-by-step guide to building a full feature using Zenflow's multi-model workflow for efficient token usage and high-quality output.

## Introduction

This guide walks through building a complete feature — a user authentication system — using Zenflow's multi-model workflow. By assigning the right model to each phase (planning, implementation, review), you get higher quality output while using tokens efficiently.

The core insight: frontier reasoning models excel at planning but are overkill for implementation. Fast models generate code efficiently when given a clear spec. Cross-model review catches issues that same-model review misses.

## Prerequisites

* A Zenflow workspace with a connected repository
* At least two [saved presets](/zenflow/orchestration/agent-presets) configured (e.g., a planner and an implementer)
* Basic familiarity with [workflows](/zenflow/task-types)

## Step 1: Set Up Your Presets

Before creating the task, configure agent presets in **Settings → Saved presets**:

| Preset Name | Agent | Model | Purpose |
| - | - | - | - |
| `planner` | Zencoder | `auto-plus` | Architecture and spec generation |
| `builder` | Zencoder | `auto` | Code implementation |
| `reviewer` | Zencoder | `auto-plus` | Cross-model code review |

<Tip>
  `auto-plus` routes to a frontier reasoning model, while `auto` routes to a fast, efficient model. Both are updated automatically as better models become available.
</Tip>

## Step 2: Create the Task

1. Click **New task** and select **Code** mode
2. Choose your repository and source branch
3. Describe the feature:

```text theme={"system"}
Build a complete user authentication system with:
- Email/password registration and login
- JWT token generation and validation
- Password hashing with bcrypt
- Protected route middleware
- Input validation for all endpoints
```

4. Select the **Multi-model** workflow
5. Click **Start**

## Step 3: Planning Phase

The Multi-model workflow starts with a planning phase using a frontier reasoning model. The agent produces:

* `spec.md` — Technical specification with architecture decisions
* `plan.md` — Implementation steps broken into discrete tasks

**What to review:**

* Are the architecture decisions sound? (e.g., JWT storage strategy, password hashing rounds)
* Does the plan cover edge cases? (expired tokens, duplicate emails, rate limiting)
* Is the scope right? (not too broad, not too narrow)

<Note>
  The planning phase is where reasoning depth matters most. A well-structured spec means the implementation phase needs fewer tokens to produce correct code — the agent doesn't have to re-derive architectural decisions.
</Note>

## Step 4: Implementation Phase

Once you approve the plan, the workflow switches to a fast model for implementation. This is the most token-intensive phase, where model efficiency has the biggest impact.

The fast model follows the spec and generates:

* Route handlers for registration, login, and token refresh
* Middleware for authentication and authorization
* Database models and migrations
* Input validation schemas
* Unit tests for each component

**Monitor the To-do panel** to track which plan steps are complete. Each step auto-commits so you can review incremental changes in the Git tab.

## Step 5: Review Phase

The workflow automatically switches to a different model for review. Cross-model review is more effective because a different model brings different assumptions and catches different classes of issues.

The reviewer evaluates against the [review rubric](/zenflow/orchestration/review-rubric):

* **Semantic resolution** — Does the implementation actually solve the requirement?
* **Contract adherence** — Do API signatures match what the spec defined?
* **Regression safety** — Could these changes break existing functionality?
* **Scope discipline** — Are there unnecessary changes outside the task scope?

## Step 6: Iterate and Merge

After review, address any findings:

1. Check the review output in the task artifacts
2. If changes are needed, provide guidance in chat — the agent iterates
3. Run your [verification script](/zenflow/project-configuration) to confirm tests pass
4. Click **Create PR** to push the branch and open a pull request

## Token Efficiency Breakdown

Here's a typical breakdown of where tokens are consumed across the three phases:

| Phase | Token share | Model type | Efficiency strategy |
| - | - | - | - |
| **Planning** | \~15% | Frontier reasoning | Invest here — quality plan reduces total tokens downstream |
| **Implementation** | \~70% | Fast model | Largest token volume — fast model executes spec without re-deriving decisions |
| **Review** | \~15% | Different model | Cross-model perspective catches issues same-model review misses |

The key efficiency gain: the spec produced in Phase 1 eliminates redundant reasoning in Phase 2. Without a spec, the implementation model spends tokens exploring architecture decisions. With a spec, it spends tokens writing code — which is what fast models do best.

## Advanced: Custom Multi-Model Workflow

For recurring projects, create a [custom workflow](/zenflow/workflows/custom) that encodes your team's specific multi-model process:

```md theme={"system"}
# Auth Feature Workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/worktrees/{task_id}`

---

## Workflow Steps

### [ ] Step: Security Architecture Review
<!-- agent: planner -->
Analyze the feature for security implications. Document threat model, 
attack vectors, and mitigations in `{@artifacts_path}/security-review.md`.

### [ ] Step: Implementation
<!-- agent: builder -->
Implement following `{@artifacts_path}/spec.md` and security review.
Include all mitigations from the security review.

### [ ] Step: Security Audit
<!-- agent: reviewer -->
Audit the implementation against the security review.
Check for OWASP Top 10 vulnerabilities.
Record findings in `{@artifacts_path}/security-audit.md`.
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Multi-Agent Orchestration" icon="arrows-split-up-and-left" href="/zenflow/multi-agent-orchestration">
    Full orchestration overview and approach comparison
  </Card>

  <Card title="Agent Presets" icon="sliders" href="/zenflow/orchestration/agent-presets">
    Configure and assign presets to workflow steps
  </Card>

  <Card title="Subagent Pipelines" icon="sitemap" href="/zenflow/orchestration/subagent-pipelines">
    Advanced parallel execution with isolated contexts
  </Card>

  <Card title="Custom Workflows" icon="sliders" href="/zenflow/workflows/custom">
    Build your own workflow templates
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.