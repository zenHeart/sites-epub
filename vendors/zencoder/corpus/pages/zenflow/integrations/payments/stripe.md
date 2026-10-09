> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stripe

> Connect Zenflow to Stripe to manage billing, subscriptions, and financial data.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

The Stripe integration gives Zenflow agents native access to your payment, subscription, billing, product, and pricing data. This allows agents to work seamlessly with customers, subscriptions, invoices, payments, products, and prices to automate financial workflows.

## Connecting to Stripe

Follow these steps to authorize and connect Stripe with Zenflow:

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar (the gear icon at the bottom left).
  </Step>

  <Step title="Find Stripe">
    Locate the **Stripe** card in the Integrations Catalog and click **Connect**.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-connect.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=f7e2a2d334e73e7ff7561daa378d2ecb" alt="Stripe Connect Card" style={{ width: "100%", maxWidth: "500px", borderRadius: "12px" }} width="625" height="146" data-path="images/integrations/stripe/stripe-connect.png" />
    </div>
  </Step>

  <Step title="Sign In to Stripe">
    A secure popup window will open requesting you to sign in to your Stripe account. Enter your email and password to authenticate.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-signin.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=a47dd1f11fa803f69bfcdf55ea2380c0" alt="Stripe Sign In Screen" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="507" height="792" data-path="images/integrations/stripe/stripe-signin.png" />
    </div>
  </Step>

  <Step title="Enable MCP Access (If prompted)">
    If Model Context Protocol (MCP) access is currently disabled for your Stripe account, click **Enable for this account** to allow Zenflow to use Stripe's secure API tools.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-enable-mcp.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=2e36c7ec800877f572ef3f1c0516c750" alt="Enable MCP Access Screen" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="504" height="788" data-path="images/integrations/stripe/stripe-enable-mcp.png" />
    </div>
  </Step>

  <Step title="Select Permissions">
    Configure the level of access you want to grant to Zenflow Stripe.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-permissions.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=31794b1ffd6584370ca5ae0622acfe0b" alt="Stripe Permissions Selection Screen" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="507" height="792" data-path="images/integrations/stripe/stripe-permissions.png" />
    </div>

    <Warning>
      **Read vs. Write Permissions: Value and Security Risks**

      * **Read-Only Access (Recommended for analysis)**: Granting "Read" access allows Zenflow agents to query customer records, fetch subscriptions, and analyze transaction data. This is ideal for generating reports, tracking metrics, and performing support tasks.
      * **Write Access (Required for action)**: Granting "Write" access enables Zenflow agents to take action on your behalf, such as creating new invoices, creating products, updating subscription tiers, or issuing refunds. Only grant "Write" permissions if you intend to authorize autonomous agent actions, and ensure you monitor agent workflows carefully.
    </Warning>

    Once you have selected your desired permissions, click **Authorize**.
  </Step>

  <Step title="Authorize Browser to Open Zenflow">
    The browser will ask for confirmation to redirect back to the Zenflow application. Click **Open Zenflow**.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-open-zenflow.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=88fa31de2cbda85cd0531ac42bd8ebac" alt="Open Zenflow Modal" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="534" height="203" data-path="images/integrations/stripe/stripe-open-zenflow.png" />
    </div>
  </Step>

  <Step title="Confirm Connected Status">
    The Stripe secure OAuth flow will show an **Integration Connected** success page which you can close.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-connected-tab.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=176192223d865b71cd5d6afc550f3a6b" alt="Integration Connected Tab Success" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="457" height="198" data-path="images/integrations/stripe/stripe-connected-tab.png" />
    </div>

    Back in your Zenflow Settings panel, Stripe will now display as **Connected (Full access)** (or the specific access level you authorized) and is ready for use by your AI agents.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/4eGYViX_AvZJ94XT/images/integrations/stripe/stripe-status-zenflow.png?fit=max&auto=format&n=4eGYViX_AvZJ94XT&q=85&s=1871ba9fbc59a8608ccfacd3d849e14b" alt="Stripe Connected Status in Zenflow" style={{ width: "100%", maxWidth: "500px", borderRadius: "12px" }} width="656" height="146" data-path="images/integrations/stripe/stripe-status-zenflow.png" />
    </div>
  </Step>
</Steps>

## What the Agent Can Do

The Stripe integration enables Zenflow agents to work with the following resources:

* **Query & Manage Customers** — Look up billing history, update details, and search customer records.
* **Track Subscriptions** — Monitor active plans, trial periods, and subscription cancellations.
* **Manage Invoices** — Create invoices, retrieve unpaid bills, and track invoice statuses.
* **Process Payments** — Retrieve payment intents, transaction details, and payout reports.
* **Configure Products & Prices** — Access, create, and update product listings and price tiers.

## Example Use Cases

* Generate daily/weekly billing reports showing new and lost revenue.
* Notify teams about subscription upgrades or failed payments.
* Look up billing, product, and subscription details during customer support tasks.
* Automatically draft custom invoices and update price plans.

## Example Automations

### Payment to Customer Lifecycle Sync

Connect Stripe and HubSpot to keep customer statuses in sync automatically:

1. **Check all new customers in Stripe**: The agent monitors Stripe for newly created customer records (requires **Read** permissions in Stripe).
2. **Sync status in HubSpot**: For any customers with an active subscription, the agent automatically searches for the corresponding contact or lead in HubSpot and updates their lifecycle stage to "Paid Customer" (requires **Write** permissions in HubSpot).

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.