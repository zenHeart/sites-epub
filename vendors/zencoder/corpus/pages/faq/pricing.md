> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing & Plans

> Zencoder usage-based pricing — plans, credits, and top-ups.

Zencoder uses a **usage-based credit model**. Every paid plan includes a flat seat price plus a monthly credit allowance. Credits are consumed by LLM usage. When you run out, you can buy top-ups at any time.

<Info>
  Premium models cost more credits per call than baseline. The cost multiplier of each model is shown in the model selector before you send.
</Info>

## Credit Usage Reference

The table below outlines typical credit consumption across different models. Real-world usage depends heavily on prompt size and codebase context.

| Model | Multiplier | Typical range (credits/request) | Avg credits | \~Requests/mo on Pro (30K) | \~Requests/mo on Pro Plus (80K) | \~Requests/mo on Pro Max (180K) |
| :- | :-: | :-: | :-: | :-: | :-: | :-: |
| **Grok Code Fast 1** | 0.25× | 10–50 | 30 | 1,000 | 2,660 | 6,000 |
| **Haiku 4.5** | 1× | 30–250 | 140 | 210 | 570 | 1,280 |
| **Auto** | 1× | 50–270 | 160 | 210 | 550 | 1,240 |
| **Gemini Flash 3.0** | 1× | 30–250 | 150 | 200 | 530 | 1,200 |
| **GPT-5.4-mini** | 1.25× | 50–260 | 220 | 135 | 360 | 810 |
| **GPT-5.3 Codex** | 2× | 30–650 | 300 | 100 | 265 | 600 |
| **Gemini Pro 3.1** | 2× | 100–650 | 500 | 60 | 160 | 360 |
| **Auto+** | 2.5× | 125–800 | 600 | 50 | 130 | 300 |
| **GPT-5.4** | 2.5× | 100–700 | 550 | 54 | 145 | 325 |
| **Gemini Flash 3.5** | 2.5× | — | — | — | — | — |
| **Sonnet 4.6** | 3× | 100–700 | 580 | 50 | 135 | 310 |
| **Opus 4.6/4.7** | 5× | 150–1,300 | 1,200 | 25 | 65 | 150 |
| **GPT-5.5** | 5× | 300–1,600 | 1,450 | 20 | 55 | 124 |

<Note>
  These are averages — a simple one-line fix uses fewer credits; a large multi-file refactor uses more. The model selector displays each model's cost multiplier before you send.

  **Telemetry data:** For newly added models (e.g., Gemini Flash 3.5), we do not yet have enough usage data to generate statistically representative averages. These will be updated as more data is collected.
</Note>

## How Many Credits Does a Typical Request Use?

<Warning>
  Credit usage varies depending on the model, the size of your prompt, and the length of the response. As a rough guide, a single request using a frontier model like Claude Sonnet 4.6 typically costs between **100 and 600 credits**, with an average around **300–400**. Simpler queries with shorter context will land on the lower end; requests involving large files or multi-step reasoning will use more. You can monitor your usage in real time from the [Usage dashboard](https://auth.zencoder.ai/profile?tab=usage).
</Warning>

### Example tasks

To give rough reference points on credit consumption please see below example tasks of different complexity. All tasks were performed on a small-to-medium full-stack web application (\~50K lines across \~200 source files; Python/FastAPI backend + React/TypeScript frontend). Size, complexity and organization of your actual codebase can affect the numbers you would get.

#### XS Task

> On the login page, change the primary 'Sign in' button background color to #3b82f6.

Simple modification across single file

| Model | Credits | Comment |
| :- | :- | :- |
| **Zencoder Auto** | 75 | Cheap model suitable for XS tasks |
| **Zencoder Auto+** | 270 | Balanced model that can be used for XS tasks |
| **Gemini 3.5 Flash** | 398 | Use for harder tasks |
| **Sonnet 4.6** | 142 | Balanced model that can be used for XS tasks |
| **Opus 4.7** | 304 | Use for hardest tasks |
| **GPT 5.5** | 456 | Use for hardest tasks |

#### S Task

> On the public session-detail page, add a 'Copy link' button next to the page title. Clicking it copies the current page URL to the clipboard and shows a success toast (use the existing toast system)

Mutliple modifications across single file

| Model | Credits | Comment |
| :- | :- | :- |
| **Zencoder Auto** | 194 | Cheap model suitable for S tasks |
| **Zencoder Auto+** | 570 | Balanced model that can be used for S tasks |
| **Gemini 3.5 Flash** | 871 | Use for harder tasks |
| **Sonnet 4.6** | 268 | Balanced model that can be used for S tasks |
| **Opus 4.7** | 575 | Use for hardest tasks |
| **GPT 5.5** | 1314 | Use for hardest tasks |

#### M Task

> Add an optional pronouns text field to the speaker profile. Persist it through the existing profile model, service, and router (no new tables — just one new column). Show it as an editable text input on the speaker profile settings page, and display it next to the speaker's name on the public profile view.

Small modifications across several backend and frontend files

| Model | Credits | Comment |
| :- | :- | :- |
| **Zencoder Auto** | 298 | Cheaper model with lower quality on more complex tasks |
| **Zencoder Auto+** | 1373 | Balanced model |
| **Gemini 3.5 Flash** | 1905 | Use for harder tasks |
| **Sonnet 4.6** | 841 | Balanced model |
| **Opus 4.7** | 1904 | Use for hardest tasks |
| **GPT 5.5** | 2675 | Use for hardest tasks |

#### L Task

> Add a 'Message speaker' action on the organizer submission-detail page. It opens a dialog with a single text area and a 'Send' button. Sending calls one new POST endpoint that creates an in-app notification of type message\_from\_organizer for the submission's speaker, with the organizer's text as the body. The notification must appear on the existing speaker Notifications page. Only the organizer of the event can call the endpoint. Do not add email delivery — in-app notification only.

Modifications across several backend and frontend files

| Model | Credits | Comment |
| :- | :- | :- |
| **Zencoder Auto** | - | Not recommended for complex tasks |
| **Zencoder Auto+** | 2059 | Balanced model |
| **Gemini 3.5 Flash** | 2812 | Higher quality model for complex tasks |
| **Sonnet 4.6** | 1305 | Balanced model |
| **Opus 4.7** | 2788 | Use for hardest tasks |
| **GPT 5.5** | 3905 | Use for hardest tasks |

#### XL Task

> Add co-speaker support to submissions. A primary speaker can invite up to 3 additional co-speakers by email when creating or editing a submission. Persist co-speakers as a new related table linked to a submission with a status of invited / accepted / declined. Add backend endpoints to list, invite (which also creates a notification), accept, and decline. On the speaker submission-detail page, show the co-speaker list with each one's status, and show 'Accept' / 'Decline' actions visible only to the invited user. On the organizer event-speakers page, include accepted co-speakers in the speaker list. Existing submission-ownership and reviewer permissions for the primary speaker must continue to work unchanged.

Substantial modifications across multiple backend and frontend files and database

| Model | Credits | Comment |
| :- | :- | :- |
| **Zencoder Auto** | - | Not recommended for complex tasks |
| **Zencoder Auto+** | 4474 | Might not be suitable for very complex tasks |
| **Gemini 3.5 Flash** | 4497 | Might not be suitable for very complex tasks |
| **Sonnet 4.6** | 4451 | Might not be suitable for very complex tasks |
| **Opus 4.7** | 7717 | Use for hardest tasks |
| **GPT 5.5** | 6299 | Use for hardest tasks |

## Workflow Credit Efficiency

The choice of workflow significantly impacts credit consumption. Standard automated tasks or focused bug fixes are highly efficient, while comprehensive design or requirements-first workflows consume more credits due to multi-step planning and deep analysis.

| Workflow | Credit Efficiency | Why |
| :- | :- | :- |
| **Auto** | Most efficient | Single-pass, model-routed |
| **Fix a Bug** | Efficient | Focused scope, shorter planning |
| **Multi-model** | Efficient | Cheaper models for bulk implementation, reserving premium models for planning |
| **Spec First** | Moderate | Two-phase: spec + implementation |
| **Requirements First** | Higher | Full PRD + spec + implementation + review |
| **Custom** | Varies | Depends on steps configured |

## Plans

| | **Free** | **Pro** | **Pro Plus** | **Pro Max** | **Enterprise** |
| :- | :-: | :-: | :-: | :-: | :-: |
| **Monthly** | \$0 | \$45 | \$95 | \$195 | Custom |
| **Annual** | \$0 | \$40/mo | \$85/mo | \$175/mo | Custom |
| **Credits / Month** | BYOK only | 30,000 | 80,000 | 180,000 | Pre-paid commit |
| **Models** | Open / Auto | All models | All models | All models | All models |

<Note>
  **Trial:** 5,000 credits for 7 days. After the trial ends, an upgrade is required to continue using bundled credits. Leftover trial credits do **not** carry over to a paid plan.
</Note>

## How Credits Work

<Info>
  **Pricing Transparency:** Credits reflect provider list pricing. When you use a Zencoder-hosted model, we pass through provider API pricing — your subscription covers the platform and Zenflow. For BYOK requests, you pay your provider directly with no credits consumed.
</Info>

### Plan Credits (included in subscription)

* Granted at the **start** of each monthly billing cycle.
* **Expire** at the end of your monthly billing period — no rollover.
* Consumed **before** top-up credits.

### Paid Top-Ups

* Bought on demand when you need more credits.
* **Non-refundable.**

<Tip>
  **Minimum top-up:** \$20
</Tip>

### Consumption Order

1. **Plan credits** (current cycle) — always first.
2. Then **top-up credits**.

## Team & Admin Controls

<AccordionGroup>
  <Accordion title="Per-user credit caps">
    Admins can set a **max-% cap** of the org credit pool per user. By default, credits are split equally across seats. Per-user overrides are supported. A user who hits their cap is blocked from further usage until the admin re-allocates or buys a top-up.
  </Accordion>

  <Accordion title="Admin re-allocation">
    Admins can re-balance credit caps between users mid-cycle. Re-allocation does not create or destroy credits — it shifts the per-user cap within the org pool.
  </Accordion>

  <Accordion title="Top-up credits for teams">
    When an admin buys a top-up, it goes into the team's shared pool. Top-up credits follow the same per-user cap rules.
  </Accordion>
</AccordionGroup>

## BYOK (Bring Your Own Key)

All plans — including Free — support **BYOK**. When you use your own API key (OpenAI, Anthropic, or Gemini), LLM calls go through your key and **do not consume bundled credits**. You still pay Zencoder the seat fee for paid plans.

## FAQ

<AccordionGroup>
  <Accordion title="What's a credit?">
    The unit of consumption inside Zencoder. Every LLM call costs a number of credits based on the model and the work involved.
  </Accordion>

  <Accordion title="Why credits and not dollars or tokens?">
    Credits decouple billing from raw token counts (which fluctuate per model and per call). One unit, one balance, one bill — predictable and easy to track.
  </Accordion>

  <Accordion title="What's the difference between Pro, Pro Plus, and Pro Max?">
    The seat price and the monthly credit allowance. All three give you access to all models. Pick the plan whose included credits cover your typical month; top up when you exceed it.
  </Accordion>

  <Accordion title="How do model costs work?">
    Premium models burn more credits per call than baseline models. The cost multiplier of the selected model is shown in the model selector before you send.
  </Accordion>

  <Accordion title="Do unused plan credits roll over?">
    No. Plan credits expire at the end of your monthly billing period.
  </Accordion>

  <Accordion title="Can I share credits across teammates?">
    Yes — paid plans use a shared org pool. Admins can set per-user caps to prevent one user from draining it.
  </Accordion>

  <Accordion title="Can I switch plans mid-cycle?">
    Yes. **Upgrade:** prorated seat-fee charge + prorated credit grant for the rest of the monthly billing period. **Downgrade:** takes effect at next monthly billing period. Current allowance is preserved until end of the current period.
  </Accordion>

  <Accordion title="What's the minimum top-up?">
    \$20 per top-up.
  </Accordion>

  <Accordion title="Are top-ups refundable?">
    No. Top-up credits are non-refundable.
  </Accordion>

  <Accordion title="Does BYOK still work?">
    Yes — every plan, including Free, supports BYOK. Calls made via your own API key do **not** consume credits. You still pay Zencoder the seat fee on paid plans.
  </Accordion>

  <Accordion title="What happens if I cancel?">
    You move to Free at the **end of the current billing period**. Plan credits are forfeited. Existing top-ups remain usable. After top-ups run out, your account is BYOK-only.
  </Accordion>

  <Accordion title="What happens if I downgrade to a lower paid plan?">
    Current cycle's allowance is preserved. The new plan's cap applies from the next cycle.
  </Accordion>

  <Accordion title="What happens if my payment fails?">
    7-day grace period (requires at least one prior successful payment). During grace: top-ups still usable, no new plan credits, no new top-ups. After grace: account moves to Free.
  </Accordion>

  <Accordion title="Are credits transferable or redeemable for cash?">
    No. Credits are not transferable, not redeemable for cash, and are only usable for Zencoder services.
  </Accordion>

  <Accordion title="Why do I see &#x22;You ran out of credits&#x22; when my dashboard still shows credits remaining?">
    Some requests require a minimum number of credits to process. If your remaining balance is below that threshold, the system cannot fulfill the request — even though a small balance is still visible on your dashboard. You can resolve this by waiting for your credits to reset, or by purchasing a credit top-up.
  </Accordion>

  <Accordion title="How many credits does a typical request use?">
    Credit usage varies depending on the model, the size of your prompt, and the length of the response. As a rough guide, a single request using a frontier model like Claude Sonnet 4.6 typically costs between 100 and 600 credits, with an average around 300–400. Simpler queries with shorter context will land on the lower end; requests involving large files or multi-step reasoning will use more. You can monitor your usage in real time from the Usage dashboard.
  </Accordion>

  <Accordion title="Can I convert my old LLM call count into credits?">
    No. The previous plan counted each LLM call as one unit regardless of its size, while credits reflect actual resource consumption — factoring in model, prompt length, and response size. A short autocomplete suggestion and a large multi-file refactor cost very different amounts, so there's no meaningful 1:1 conversion between the two systems.

    As a rough guide: a typical request using a frontier model like Claude Sonnet 4.6 costs between 100 and 600 credits (averaging around 300–400). Lighter tasks cost less; complex, context-heavy requests cost more.
  </Accordion>
</AccordionGroup>

## Legacy Plans (Migration)

The old per-seat, daily-call plans are being retired. If you're currently on a legacy plan, you'll be automatically migrated to a usage-based plan at a future renewal. If you'd prefer to switch sooner, you can do so from your [profile](https://auth.zencoder.ai).

| Old Plan | Old Price (mo / yr) | Daily Call Limit | New Plan |
| :- | :- | :- | :- |
| Free | \$0 | 30 calls/day | **Free** (BYOK) |
| Starter | $19 / $17 | 280 calls/day | **Pro** (\$45 / \$40) |
| Core | $49 / $44 | 750 calls/day | **Pro** or **Pro Plus** (\$45–\$95) |
| Advanced | $119 / $107 | 1,900 calls/day | **Pro Plus** or **Pro Max** |
| Max | $250 / $225 | 4,200 calls/day | **Pro Max** (\$195 / \$175) |
| Enterprise | Custom | Custom | **Enterprise** |

<Info>
  If you've already paid for an annual seat, you're **grandfathered until renewal**. Nothing changes mid-contract.
</Info>

<AccordionGroup>
  <Accordion title="I'm on an old annual contract — what happens?">
    Grandfathered until renewal. Your seat price and call limits stay until end of contract. We'll contact you \~30 days before renewal.
  </Accordion>

  <Accordion title="I'm on an old monthly plan — when do I move?">
    At your next renewal date after the announcement. You'll get 30 days' notice.
  </Accordion>

  <Accordion title="Will my price go up?">
    For most customers, no. For some heavy users on Advanced/Max, the new equivalent plan will be **lower priced** but with credit-metered consumption.
  </Accordion>
</AccordionGroup>

## Payment Methods

Zencoder accepts:

* All major credit cards
* Apple Pay
* Link
* Cash App and Klarna

For wire transfers or enterprise invoicing, [contact our support team](/get-started/community-support).

## Refund Policy

Top-up credits are **non-refundable**. For subscription-related refund questions, see our [Refund Policy](/faq/refund-policy).

<Info>
  Questions? See our [Trust Center](https://trust.zencoder.ai) for security details or reach us on [Discord](https://discord.gg/zencoder).
</Info>

[Get Started Now →](https://auth.zencoder.ai/signup)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.