> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Review Rubric

> Structured evaluation criteria for AI code review steps — paste into review step instructions for consistent, measurable feedback.

## Overview

Use this rubric when configuring your review step instructions — paste it into the step description so the reviewer has a structured framework to evaluate against. It works with both [preset-based](/zenflow/orchestration/agent-presets) review steps and [Subagent-based](/zenflow/orchestration/subagent-pipelines) review workers.

The rubric evaluates on two axes:

## Delivery — Did the Implementation Solve the Problem?

| Criterion | What to check |
| - | - |
| **Semantic resolution** | Does the patch fix the actual root cause, or does it paper over the symptom? |
| **Contract adherence** | Do public signatures, return types, error types, and API shapes match what the codebase expects? |
| **Integration completeness** | Are all affected call sites, validators, serializers, schemas, and compatibility layers updated? |

## Engineering — Is the Implementation Safe and Maintainable?

| Criterion | What to check |
| - | - |
| **Regression safety** | Does the patch break anything that previously worked? Look for changed signatures, removed validation, altered error behavior. |
| **Scope discipline** | Is every change in the diff justified by the task? Unnecessary refactoring, extra features, and unrelated cleanup hurt here. |
| **Maintainability** | Is the code idiomatic for the repository? Is the logic clear? Are there dead paths, duplication, or half-finished constructs? |

A patch can score well on one axis and poorly on the other. Code can solve the problem correctly but be unsafe to merge. Code can be clean and focused but miss half the required changes. Evaluating both independently gives a more useful signal than a single pass/fail.

## Scoring

Score each criterion on this scale:

| Score | Meaning |
| - | - |
| **0 — Inadequate** | Weak on this dimension |
| **1 — Partial** | Meaningful progress, but significant gaps remain |
| **2 — Solid** | Generally good, only limited issues |
| **3 — Excellent** | Very strong result |

## Interpreting Results

| Overall assessment | When |
| - | - |
| **Merge-ready** | Both axes score ≥ 2 across all criteria |
| **Small follow-up** | One criterion is partial but the gap is bounded |
| **Substantial rework** | Multiple criteria have gaps or semantic resolution is only partial |

## Using the Rubric in Workflow Steps

Paste the criteria directly into your review step description so the agent evaluates against them:

```md theme={"system"}
### [ ] Step: Review
<!-- agent: sonnet-reviewer -->
Review all changes against the spec. Evaluate on two axes:

**Delivery**: semantic resolution, contract adherence, integration completeness.
**Engineering**: regression safety, scope discipline, maintainability.

Score each criterion 0–3. A patch is merge-ready when both axes score ≥ 2.
Record findings in `{@artifacts_path}/review.md`.
```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.