> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automations

Tell Manus what should happen and when. It can run the work on a schedule, respond when something happens in a connected app, or turn a plain-language request into a multi-step automation. You describe the outcome; Manus handles the workflow.

<img src="https://mintcdn.com/docs-manus/zKF_C2e0jUQseFr5/images/image-6.png?fit=max&auto=format&n=zKF_C2e0jUQseFr5&q=85&s=d2fa6a209626d3c8a47e1698c759ab4c" alt="Image" width="2978" height="1638" data-path="images/image-6.png" />

## What it is

Automations let Manus keep work moving without waiting for you to start every task manually.

| Automation type | Starts when | Try it for |
| :- | :- | :- |
| Schedule | A time you choose | Daily briefs, weekly reports, recurring research, and one-time reminders |
| Triggered task | A selected event happens | Auto-reviewing a new GitHub pull request, responding to a Shopify refund, processing an invoice email, or preparing for a calendar event |
| Advanced automation (Beta) | Manus turns your natural-language request into a workflow | Work that brings together several sources, conditions, and actions |

The main difference is what starts the work. A Schedule starts from time. A Triggered task starts from an event. An Advanced automation lets you describe the whole routine naturally and have Manus configure it for you.

## How to Create Automations

#### From the left sidebar

Click Automations, then Create. Choose Schedule, Trigger, or Advanced automation.

This route is best when you want to see existing automations, recent runs, and management controls before creating something new.

#### From Build

From the Manus home page, click Build, then choose Automations under Other.

You will land on the same creation experience, where you can choose how the automation starts.

### Create a schedule

<img src="https://mintcdn.com/docs-manus/zKF_C2e0jUQseFr5/images/image-7.png?fit=max&auto=format&n=zKF_C2e0jUQseFr5&q=85&s=6bb1fde1272ae64ea14ea152ecf4a6f1" alt="Image" width="2996" height="1640" data-path="images/image-7.png" />

Choose Schedule when the work belongs to a time: every weekday morning, every Friday afternoon, on the first day of the month, or once at a specific date and time.

Set the timing, then describe the result you want in Manus will. You can write the request as naturally as you would in any Manus task.

Every weekday at 5 PM Singapore time, review today’s open tasks and meetings. Summarize what was completed, list anything that still needs follow-up, and send me a concise end-of-day review.

Use a specific time and timezone when timing matters. “Every weekday at 5 PM Singapore time” is more reliable than “at the end of the day.”

### Create a triggered tas

<img src="https://mintcdn.com/docs-manus/zKF_C2e0jUQseFr5/images/image-8.png?fit=max&auto=format&n=zKF_C2e0jUQseFr5&q=85&s=c01ef23620d68275b262fbbb93528477" alt="Image" width="2996" height="1636" data-path="images/image-8.png" />

Choose Triggered task when Manus should act because something happened: a pull request opened, a refund was created, an invoice arrived, or a meeting is approaching.

Select the app or event source, choose the event, and describe what Manus should do. Add conditions when only some events should qualify. The condition fields shown in the setup are validated for the selected trigger, so you can filter using supported details such as repository, branch, label, sender, amount, or status.

The picker can include Gmail, Outlook Mail, Mail Manus, Notion, Google Calendar, Outlook Calendar, GitHub, Shopify, Google Workspace, advertising platforms, RSS, Webhook, and other available sources. What you see depends on your connected apps and product availability.

#### Review new GitHub pull requests

When: A pull request is opened or marked ready for review in the selected repository.

Only if: The base branch is main and the pull request is not a draft.

Summarize the change, identify high-risk files, and check whether the main behavior is covered by tests. Put blocking issues first. Post a review only when there is a clear actionable finding; otherwise send the summary to me in Manus.

GitHub is a strong fit when the work should react to repository activity as it happens.

#### Follow up after a Shopify refund

When: A refund is created in Shopify.

Only if: The refund is greater than \$100 or the customer has placed more than three previous orders.

Review the order, refund reason, and customer history. Draft a personalized follow-up that acknowledges the issue and recommends the best next step. Send the draft to the customer-support channel for review.

Shopify is a strong fit for event-driven store work such as new orders, refunds, fulfillment changes, and inventory updates.

#### Log invoice emails

When: A new invoice or receipt email arrives.

Only if: The message has an attachment and the sender or subject matches your billing rules.

Extract the merchant, invoice number, date, currency, subtotal, tax, and total. Add one row to the finance spreadsheet, save the attachment to the invoice folder, and flag any missing fields for review.

### Create an advanced automation

<img src="https://mintcdn.com/docs-manus/zKF_C2e0jUQseFr5/images/image-9.png?fit=max&auto=format&n=zKF_C2e0jUQseFr5&q=85&s=c8d2de5cd2990664141b9ef6e344bdc4" alt="Image" width="2982" height="1636" data-path="images/image-9.png" />

Advanced automations are the most direct way to turn a complete idea into a workflow. Open Automations → Create → Advanced automation, then describe the routine in natural language. You can also ask Manus directly in a new or existing task.

> Create an automation for our weekday operations review. At 5 PM, collect open GitHub pull requests, Shopify refunds created that day, and unresolved support messages. Group the findings by owner, highlight anything blocking a customer or release, update the operations page in Notion, and send a five-bullet summary to the team channel.

A useful request says when Manus should act, what information it should use, which cases matter, and where the result should go. You do not need to map every step yourself. After Manus builds the automation, review the generated timing, conditions, actions, and accounts before activating it.

## Managing Your Automations

### See what ran

Open Automations → Updates to see the latest runs grouped by date. Each entry shows the automation, run time, status, and a short result summary. Open a run to inspect the full result or find out why it needs attention.

Switch to the calendar icon in the upper-right corner when you want a month-level view of activity and upcoming scheduled work. Use the arrows to change months, Today to return to the current date, and the more link to expand a busy day.

### Manage and test automations

Open Automations → Manage to see active schedules and triggers. Each card shows its type, connected app, status, name, and instructions.

Open the More actions menu to pause the automation, run a test, locate its original task, edit it, or delete it.

Use Test run before relying on a new automation and after changing its timing, conditions, instructions, or connected account. For a trigger, test one event that should match and one that should not.

## Differences between automation types

| If you want Manus to… | Use | Why |
| :- | :- | :- |
| Run at a specific time | Schedule | Time is what starts the work |
| React when something happens | Triggered task | An event is what starts the work |
| Turn a complete plain-language idea into a workflow | Advanced automation | Manus configures the routine from your description |

Scheduled tasks, available on Manus previously, continue to work in the unified Automations feature. These are tasks that run solely based on time.

A Triggered task runs based on an event, or perhaps when the source is checked periodically. Supported GitHub, Shopify, Webhook, and Mail Manus events can be delivered as they happen. Several other connected apps are checked for new events approximately at intervals, so those triggers may not start instantly.

Advanced automations can include a combination of several connectors, conditions and trigger types. Initiating by natural language is enough to set up such workflows.

## Tips for reliable automations

1. Describe the outcome, not the plumbing. Tell Manus what should happen, what a good result looks like, and where it should go.
2. Make the event specific. “When a refund over \$100 is created” is clearer than “when something changes in Shopify.”
3. Say what not to act on. Conditions are especially useful for excluding drafts, internal senders, small transactions, or completed items.
4. Define the exception path. Tell Manus what to do when information is missing, confidence is low, or an external action needs review.
5. Test realistic cases. Check the expected path, a filtered-out event, connector access, and the final destination.
6. Check Updates after changes. A quick review confirms that the new version ran and produced the intended result.

## Frequently Asked Questions

### Do I have to build every automation manually?

No. For an Advanced automation, describe the routine directly in Manus or choose Automations → Create → Advanced automation. Manus will turn the request into a workflow for you to review.

### Why did my triggered task not start immediately?

Some sources deliver supported events as they happen, while others are checked periodically. Also confirm that the connector is authorized and that the event matches every condition you added.

### Can every connected app use the same events and conditions?

No. Each source exposes its own supported events and condition fields. The creation flow shows the options currently validated for the selected trigger and account.

### What should I do if an automation needs attention?

Open its latest run in Updates and review the error. Reauthorize the connector or correct the instructions and conditions, then use Test run before resuming it. A trigger can pause after the same failure repeats across several checks.

### Can an automation keep using the context from an existing task?

When the run option is available, choose to continue in the same task. This is useful when the automation depends on earlier messages, files, decisions, or an artifact that should keep being updated. Choose a new task when each run should be independent.

### What happened to my existing scheduled tasks?

They continue to run and now appear alongside triggers and advanced automations in Automations. They remain schedules and keep their time-based behavior.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.