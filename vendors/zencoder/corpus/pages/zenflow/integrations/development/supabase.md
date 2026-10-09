> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Supabase

> Connect Zenflow to Supabase to query databases, manage auth, and list storage files.

<span className="set-page-badge-extended" />

<Note>
  This extended integration requires a paid Zencoder account.
</Note>

## Overview

The Supabase integration gives Zenflow agents access to your Supabase databases, authentication, and storage services. Run SQL queries, manage database tables, list users, and fetch storage files directly from your agent.

## Connecting Supabase

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Search for Supabase">
    Locate **Supabase** in the Integrations Catalog and click the **Connect** or **\[+]** button.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-card.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=e0d68679ba1e8ffa0e54e42782a36495" alt="Supabase Integration Card" style={{ width: "100%", maxWidth: "500px", borderRadius: "12px" }} width="560" height="140" data-path="images/integrations/pipedream-card.png" />
    </div>
  </Step>

  <Step title="Consent to Connection">
    A secure popup window will open asking for permission to connect your account. Click **Continue** to proceed.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-consent.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=8bef370f3584515ee91bdb286c558acc" alt="Pipedream Consent Screen" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="388" height="576" data-path="images/integrations/pipedream-consent.png" />
    </div>
  </Step>

  <Step title="Authorize Connection">
    Provide your Supabase Project URL and Service Role Key (or API Key) in the connection popup.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-apikey-connect.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=a7d3ff6be2aa952fb56f9284d1cad83f" alt="API Key Connection Screen Example" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="388" height="576" data-path="images/integrations/pipedream-apikey-connect.png" />
    </div>
  </Step>

  <Step title="Complete Setup">
    A progress window will briefly indicate that the account connection is in progress, followed by a confirmation.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-connecting.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=551313855862e9f99e2b409748d16a21" alt="Connection in Progress" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="388" height="576" data-path="images/integrations/pipedream-connecting.png" />
    </div>

    Once authorized, close the popup. The integration will instantly display as **Connected** in your Zenflow dashboard and is active for your AI agents.
  </Step>

  <Step title="Test Connection">
    Verify connection status and test query permissions to ensure everything is working.
  </Step>
</Steps>

## What the Agent Can Do

* **Execute SQL** — Run queries, select records, and execute database functions
* **Manage Users** — Retrieve user profiles, check auth status, and reset passwords
* **Manage Files** — List storage buckets, download files, and upload assets
* **Sync Tables** — Keep external systems in sync with your database tables

## Example Use Cases

* Automatically run schema migrations or inspect table structures
* Retrieve aggregate metrics (e.g., total active signups) for daily briefings
* Sync CRM contact details to your Supabase users database
* Clean up or archive inactive database records on a regular schedule

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.