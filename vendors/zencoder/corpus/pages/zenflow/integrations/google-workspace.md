> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Workspace

> Connect Zenflow to Google Suite (Gmail, Calendar, Google Drive) to read, draft, and send emails autonomously; read events, check availability, and create invites; search, read, create, and organize documents.

<span className="set-page-badge-native" />

## Overview

The Google suite integrations let the AI agent interact with your:

* email directly. Search threads, read messages, draft replies, and send emails — all from within a Zenflow task.
* calendar. It can check schedules, find availability, create events, and set reminders — enabling automated meeting prep, scheduling workflows, and time-based task triggers.
* files and documents. Search across Drive, read and create Google Docs, Sheets, and Slides, organize folders, and generate reports, proposals, and summaries.

## Permissions

Gmail supports two permission levels:

| Permission | What the agent can do |
| - | - |
| **Read only** | Search inbox, read email threads, extract information from messages and attachments |
| **Read & Write** | Everything in Read only, plus draft emails, save drafts for review, and send messages |

Google Calendar supports two permission levels:

| Permission | What the agent can do |
| - | - |
| **Read only** | Read events, check availability |
| **Read & Write** | Everything in Read only, plus create calendar invites, set reminders, and manage recurring events |

Google Drive currently supports **Read & Write** only.

## Connecting to Google Workspace

### Step 1: Set Up Google Cloud OAuth (once for all integrations)

Google Workspace integrations require OAuth credentials from a Google Cloud project. Follow these steps to create them:

<Steps>
  <Step title="Create or select a Google Cloud project">
    Go to the [Google Cloud Console](https://console.cloud.google.com/)

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/main-page.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=348fce7a6ed1be1e7cbfa7bdc1e03682" alt="google cloud main page" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/main-page.png" />

    Create a new project or select an existing one

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/project-selector-create.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=a6ff06ffadd368ad76133a95c927bf07" alt="google cloud project selector" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/project-selector-create.png" />
  </Step>

  <Step title="Create an OAuth consent screen">
    Go to [Create OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent) or search for **OAuth consent screen** in the search bar

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/oauth-consent-screen-search.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=5c1c672ff41a9d8d254d6da394ca266b" alt="google cloud search bar" width="2608" height="539" data-path="images/integrations/google-suite/oauth-setup/oauth-consent-screen-search.png" />

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/oauth-overview-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=afe3a51828bf327b21daca7810a7e592" alt="google cloud search bar" width="3456" height="1291" data-path="images/integrations/google-suite/oauth-setup/oauth-overview-screen.png" />

    Click **Get started**, fill in the required info, make sure to put **Audience** on a second screen to external

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/project-config1.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=f8ab4bd7a976316cc68ea9356be46bc5" alt="google cloud oauth project config step 1" width="1360" height="1477" data-path="images/integrations/google-suite/oauth-setup/project-config1.png" />

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/project-config2.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=b53827dedd9798fbfc22a989a1918337" alt="google cloud oauth project config step 2" width="1195" height="1793" data-path="images/integrations/google-suite/oauth-setup/project-config2.png" />

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/project-config3.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=472e5ca41b9abfb8fee65f4432558d21" alt="google cloud oauth project config step 3" width="1188" height="1313" data-path="images/integrations/google-suite/oauth-setup/project-config3.png" />

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/project-config4.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=457ed3b62ff50112f7673f3f06425691" alt="google cloud oauth project config step 4" width="995" height="1211" data-path="images/integrations/google-suite/oauth-setup/project-config4.png" />
  </Step>

  <Step title="Add your email as a test user">
    Go to the **Audience** page and add your Google email under **Test users**.

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/audience.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=b7b0865df6eb25d2d86214b75f94ab76" alt="google cloud audience screen" width="1184" height="2029" data-path="images/integrations/google-suite/oauth-setup/audience.png" />

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/audience-add-user.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=f640852eeb91c09d02091976f782e369" alt="google cloud audience screen adding user" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/audience-add-user.png" />
  </Step>

  <Step title="Create OAuth client credentials">
    Go to **Clients**, click **Create Client**, select **Desktop app** as the application type, give desired na,e, and click **Create**.

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/oauth-client-create.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=8e70585ce6a393fb844b6e6e3092d17d" alt="google cloud client creation" width="1181" height="1039" data-path="images/integrations/google-suite/oauth-setup/oauth-client-create.png" />
  </Step>

  <Step title="Copy your credentials">
    Copy the **Client ID** and **Client Secret** from the created credential. You will need these in the next step.

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/oauth-client-created.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=e85e2a923cb984e61bdc1b99a3f59e3d" alt="google cloud client creation" width="1041" height="1322" data-path="images/integrations/google-suite/oauth-setup/oauth-client-created.png" />
  </Step>
</Steps>

### Step 2: Enable required APIs

Enable APIs for corresponding integrations that you want to enable. When opening links, make sure the project is set to the correct one in the dropdown in the top left corner

<Steps>
  <Step title="Gmail">
    Navigate to [Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com), click **Enable**

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/gmail-api-enable.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=e667f53fdce9ab78ed488dac17bcc478" alt="google cloud gmail api enable screen" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/gmail-api-enable.png" />
  </Step>

  <Step title="Google Calendar">
    Navigate to [Google Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com), click **Enable**

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/calendar-api-enable.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=bbad742dcd3d1e21ea63fc2cbebb74ac" alt="google cloud gmail api enable screen" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/calendar-api-enable.png" />
  </Step>

  <Step title="Gmail">
    Navigate to [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com), click **Enable**

    <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/oauth-setup/drive-api-enable.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=8c376bc121d381158a9e056eeef4b441" alt="google cloud gmail api enable screen" width="3456" height="2234" data-path="images/integrations/google-suite/oauth-setup/drive-api-enable.png" />
  </Step>
</Steps>

### Step 3: Connect in Zenflow

<Tabs>
  <Tab title="Gmail">
    <Steps>
      <Step title="Open Settings & Integrations">
        Navigate to **Settings → Integrations** in the Zenflow sidebar (the gear icon at the bottom left).
      </Step>

      <Step title="Find Gmail">
        Locate **Gmail** in the Integrations Catalog.
      </Step>

      <Step title="Choose your permission level">
        Select **Read only** or **Read & Write** from the dropdown depending on your needs.

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/access-level-dropdown.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=37b4d172ea08f64ca6786477509a09e0" alt="gmail integration access level" width="1752" height="453" data-path="images/integrations/google-suite/gmail/access-level-dropdown.png" />
      </Step>

      <Step title="Click Connect and enter credentials">
        Click **Connect**, paste your **Client ID** and **Client Secret** from OAuth client created above, then click **Next**, enable Gmail API if haven't done so yet (see Step 2 above) and click **Connect**

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/connect-first-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=3fac55034b354bbc70afe1c037ac97e4" alt="gmail credentials entry form" width="1139" height="1146" data-path="images/integrations/google-suite/gmail/connect-first-screen.png" />

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/connect-second-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=3669207221fe8c32c395ba72e9768d86" alt="gmail api enable link" width="1131" height="381" data-path="images/integrations/google-suite/gmail/connect-second-screen.png" />
      </Step>

      <Step title="Choose an account">
        You will be redirected to a webpage where you need to select which account you want to connect

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/choose-an-account.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=f922b9c7d499a9d54cd31b010978165c" alt="gmail choose an account screen" width="2166" height="1119" data-path="images/integrations/google-suite/gmail/choose-an-account.png" />
      </Step>

      <Step title="Allow access">
        After choosing an account, you'll be redirected to the access authorization screen. If you've chosen **Read only** your scopes might be different from the screenshot below (it is for **Read & Write**)

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/allow-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=e41e9bf267fca7e49728038ff158f9ab" alt="gmail allow access screen" width="2113" height="1691" data-path="images/integrations/google-suite/gmail/allow-screen.png" />
      </Step>

      <Step title="Integration enabled">
        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/gmail/connected-integration-zenflow.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=9c3d728f238a6a52173c3c456fd1146f" alt="gmail integration connected" width="1704" height="186" data-path="images/integrations/google-suite/gmail/connected-integration-zenflow.png" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Google Calendar">
    <Steps>
      <Step title="Open Settings & Integrations">
        Navigate to **Settings → Integrations** in the Zenflow sidebar.
      </Step>

      <Step title="Find Google Calendar">
        Locate **Google Calendar** in the Integrations Catalog.
      </Step>

      <Step title="Choose your permission level">
        Select **Read only** or **Read & Write** from the dropdown depending on your needs.

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/access-level-dropdown.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=360b1b0c15d2a7438759fc76e6a1dca2" alt="google calendar integration access level" width="1691" height="371" data-path="images/integrations/google-suite/calendar/access-level-dropdown.png" />
      </Step>

      <Step title="Click Connect and enter credentials">
        Click **Connect**, paste your **Client ID** and **Client Secret** from OAuth client created above, then click **Next**, enable Google Calendar API if haven't done so yet (see Step 2 above) and click **Connect**

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/connect-first-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=ae70d4af6b8dc68e3365c5c18c360363" alt="google calendar credentials entry form" width="1138" height="1148" data-path="images/integrations/google-suite/calendar/connect-first-screen.png" />

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/connect-second-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=14fe3b4b2ac9d205ebfe28ad1b2836a6" alt="google calendar api enable link" width="1151" height="375" data-path="images/integrations/google-suite/calendar/connect-second-screen.png" />
      </Step>

      <Step title="Choose an account">
        You will be redirected to a webpage where you need to select which account you want to connect

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/choose-an-account.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=5b78d4adc88682a9bae30ea6d7513f43" alt="google calendar choose an account screen" width="2166" height="1119" data-path="images/integrations/google-suite/calendar/choose-an-account.png" />
      </Step>

      <Step title="Allow access">
        After choosing an account, you'll be redirected to the access authorization screen. If you've chosen **Read only** your scopes might be different from the screenshot below (it is for **Read & Write**)

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/allow-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=5dbafc20cbb2f7bd7d53ad89dbc68870" alt="google calendar allow access screen" width="2095" height="1766" data-path="images/integrations/google-suite/calendar/allow-screen.png" />
      </Step>

      <Step title="Integration enabled">
        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/calendar/connected-integration-zenflow.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=d69d8b8537609a1ff024e5e083741875" alt="google calendar integration connected" width="1698" height="183" data-path="images/integrations/google-suite/calendar/connected-integration-zenflow.png" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Google Drive & Docs">
    <Steps>
      <Step title="Open Settings & Integrations">
        Navigate to **Settings → Integrations** in the Zenflow sidebar.
      </Step>

      <Step title="Find Google Drive & Docs">
        Locate **Google Drive & Docs** in the Integrations Catalog.
      </Step>

      <Step title="Click Connect and enter credentials">
        Click **Connect**, paste your **Client ID** and **Client Secret** from OAuth client created above, then click **Next**, enable Google Drive API if haven't done so yet (see Step 2 above) and click **Connect**

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/drive/connect-first-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=82eb6506e5558a5d76c046d3743d1c5d" alt="google drive credentials entry form" width="1141" height="1147" data-path="images/integrations/google-suite/drive/connect-first-screen.png" />

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/drive/connect-second-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=1eb982c3a0dcc3641226904bbd2af4c2" alt="google drive api enable link" width="1128" height="364" data-path="images/integrations/google-suite/drive/connect-second-screen.png" />
      </Step>

      <Step title="Choose an account">
        You will be redirected to a webpage where you need to select which account you want to connect

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/drive/choose-an-account.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=025fb36244ff7f892b34272c3704031f" alt="google drive choose an account screen" width="2166" height="1119" data-path="images/integrations/google-suite/drive/choose-an-account.png" />
      </Step>

      <Step title="Allow access">
        After choosing an account, you'll be redirected to the access authorization screen.

        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/drive/allow-screen.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=8578f3fbf4eaff1300fbbe7b192b80ad" alt="google drive allow access screen" width="2108" height="1409" data-path="images/integrations/google-suite/drive/allow-screen.png" />
      </Step>

      <Step title="Integration enabled">
        <img src="https://mintcdn.com/forgoodaiinc/nTupqOmI1rm5ntqv/images/integrations/google-suite/drive/connected-integration-zenflow.png?fit=max&auto=format&n=nTupqOmI1rm5ntqv&q=85&s=24c824d095bd389cda2b78d68a4bb1fa" alt="google drive integration connected" width="1699" height="177" data-path="images/integrations/google-suite/drive/connected-integration-zenflow.png" />
      </Step>
    </Steps>
  </Tab>
</Tabs>

## What the Agent Can Do

### Gmail

* **Search** — Find emails by keyword, sender, recipient, date range, or label
* **Read** — Open and read full email threads including attachments
* **Draft** — Compose new emails or replies and save them as drafts for your review before sending
* **Send** — Send emails directly (requires Read & Write permission)

### Google Calendar

* **Read events** — View upcoming meetings, attendees, and event details
* **Check availability** — Find open time slots across your calendar
* **Create events** — Schedule meetings, add attendees, and set locations or video links
* **Set reminders** — Create calendar reminders and recurring events

### Google Drive & Docs

* **Search** — Find files and folders across your Google Drive by name, content, or type
* **Read** — Open and read Google Docs, Sheets, and Slides
* **Create** — Generate new documents, spreadsheets, and presentations
* **Update** — Edit existing documents with new content
* **Organize** — Create folders and move files into structured locations
* **Write reports** — Generate briefs, proposals, summaries, and formatted documents

## Example Use Cases

### Gmail

* Draft follow-up emails to prospects after sales calls
* Scan inbox for customer feedback or churn signals
* Compile weekly digest emails from project updates
* Auto-draft replies to common inquiries

### Google Calendar

* Prepare meeting briefs by pulling context from calendar events
* Schedule follow-up meetings after sales calls
* Create onboarding calendar events for new hires
* Coordinate content publishing schedules

### Google Drive & Docs

* Compile weekly executive briefs from multiple data sources into a Google Doc
* Create proposal drafts from email threads and save to a shared Drive folder
* Build expense reports by extracting data from Gmail receipts into Sheets
* Organize meeting notes into structured folders by team and date

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.