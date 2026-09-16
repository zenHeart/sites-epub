#### Manage and protect

# Settings and notifications

Use Grok Bot settings for app-wide and desktop-local behavior, and conversation
details for one Bot's profile and notifications.

## Open Grok Bot settings

Open the account menu and choose **Settings**, or press `Cmd/Ctrl+,`.

The **Grok Bot settings** dialog contains sections based on your account and
rollout. Some options described below may not appear.

## General

### Account

Sign in or out of the Cursor account used by Grok Bot. The account menu also
shows **About**, the installed Grok Bot version, and a link to the iOS or
Android app.

### Appearance

Choose **Follow System**, **Light**, or **Dark**.

### Agent

Configure shared and local Bot behavior:

* **Timezone**, which routines use for schedules
* **Execution on Local Computer**

Cursor manages model selection, so there is no model picker.

### Auto-review

Manage your personal Auto Review rules.

Two settings in **General** deserve care. **Execution on Local Computer**
controls whether Bots can run commands on the desktop in front of you;
per-command approval is the default, and the setting applies to that desktop
alone. Auto Review rules shape which actions stop for your approval, and they
are stored on the current desktop and synced to its Grok Bot computer. Either
way, do not assume another desktop installation carries the same configuration.
Read [Approvals, security, and privacy](/grok-bot/approvals-security-and-privacy)
before changing either.

## Plugins

Use **Marketplace** to discover plugins and packaged skills. Use **Yours** to
review installed plugins and private skills.

An installed plugin may still need browser authentication. Individual plugin
tools can be enabled or disabled. On the Teams plan and the Enterprise plan,
team-provided plugins may be required or restricted by an admin.

See [Connect plugins](/grok-bot/computer-and-apps#connect-an-app) for the
connection flow.

## Usage and billing

**Usage & Billing** shows weekly included usage and on-demand usage for eligible
accounts, and the account menu can show **Weekly usage** at a glance. If neither
surface appears, review usage from the Cursor account page or contact your
organization's admin.

For how plans, weekly usage, and on-demand spend work, see
[Plans and billing](https://cursor.com/help/grok-bot/plans).

## Team Setup

On the Teams plan and the Enterprise plan, **Team Setup** shows the managed
setup your admin provides for team computers. You can review or reinstall the
current setup. Admins configure it from the dashboard; see
[Grok Bot for teams and enterprises](/grok-bot/teams-and-enterprises#set-up-your-team).

Do not place secret values directly in managed setup instructions.

## Beta and updates

The update controls live in the **Beta** section of settings, alongside
security-key or egress-routing options when those are available. The Grok Bot
app and the Agent Computer update separately:

* **Check for Updates** and **Restart to Update** update the desktop app.
* **Update Agent Computer** rebuilds the cloud computer on the latest image
  while preserving durable state.
* **Reset Agent Computer** is a last resort that returns the computer to its
  synced durable state; unsynced recent work does not come back.

See [Troubleshooting](/grok-bot/troubleshooting) for the least destructive
recovery order.

## Edit one Bot

Open **View conversation details**, then **Agent settings**, to edit that Bot's:

* Name, title, and description
* Avatar
* **Notifications** preference

These settings belong to one Bot. **Execution on Local Computer** and
Auto-review settings are shared across Bots using the current setup, but are not
an account-synchronized policy across every device.

## Understand attention states

The sidebar distinguishes:

* **Needs attention** for a question, approval, or handoff
* **Unread activity** for a new result
* Working or typing status

Opening a conversation marks its current activity as read. Use the Bot menu to
mark a conversation read or unread manually.

## Control notifications

Turn on **Notifications** in a Bot's settings to receive an operating-system or
mobile notification when that Bot finishes or needs input. Group chats do not
have the same per-Bot notification switch.

Notifications are normally suppressed while Grok Bot is focused. The sidebar
and dock badge still show unread activity.

The iPhone and Android apps also ask for notification permission during first
run. Both device permission and the Bot's notification setting must allow the
notification. Mobile push delivery is rolling out and may not yet be enabled
for every account.

## Handle in-app errors

Errors appear above the composer under **Notifications**. You can dismiss one
notice or clear the list. Some notices include **Copy request ID** for support;
copy and share the complete ID with
[support](/grok-bot/troubleshooting#before-contacting-support).

Clearing a notice removes the notification, not the underlying external action
or Bot history.

## Related pages

* [Use the computer and apps](/grok-bot/computer-and-apps)
* [Approvals, security, and privacy](/grok-bot/approvals-security-and-privacy)
* [Grok Bot for teams and enterprises](/grok-bot/teams-and-enterprises)
* [Plans and billing](https://cursor.com/help/grok-bot/plans)
* [Remove access and working data](/grok-bot/approvals-security-and-privacy#remove-access-and-working-data)
