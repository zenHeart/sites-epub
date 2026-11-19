> ## AI Agent Context
> Get the complete documentation index at: https://aistudio.google.com/llms.txt
> Use this file to discover all available pages.
> For the full documentation in a single file, fetch: https://aistudio.google.com/llms-full.txt

# Custom domains in Google AI Studio

Web apps published in Google AI Studio Build mode receive a free `ai.studio`
subdomain. You can also buy and connect your own custom domain, such as
`example.com`, from the **Publish** panel.

AI Studio registers your domain through
[Cloud Domains](https://cloud.google.com/domains) and configures
[Cloud DNS](https://cloud.google.com/dns) routing in your Google Cloud project.
It then creates a managed SSL certificate for your
[Cloud Run](https://cloud.google.com/run) service.

{% button href="https://aistudio.google.com/apps" variant="ais" %}Open Build in AI Studio{% /button %}

## Prerequisites  {% id="prerequisites" %}

Before you purchase or attach a custom domain, confirm your project meets these
three requirements:

1. **Paid Google Cloud project**: Custom domains require a
  [paid Google Cloud project](/docs/aistudio-deploying#standard-deployment)
  with an active Cloud Billing account. Custom domains are not available on the
  [Google Cloud Starter Tier](/docs/aistudio-deploying#about-the-starter-tier).
  If your app uses Starter Tier, click **Upgrade to continue** on the **Custom
  domains** card in the **Publish** panel to attach a billing account.
2. **IAM permissions**: Your Google Account needs **Owner** (`roles/owner`) or
  **Editor** (`roles/editor`) on the project. Alternatively, grant **Cloud
  Domains Admin** (`roles/domains.admin`), **DNS Administrator**
  (`roles/dns.admin`), and **Cloud Run Admin** (`roles/run.admin`). If the
  Cloud Domains, Cloud DNS, and Cloud Run APIs aren't enabled, grant **Service
  Usage Admin** (`roles/serviceusage.serviceUsageAdmin`) or
  `serviceusage.services.enable`.
3. **Available domain registration quota**: Each Google Cloud project has a
  default limit on active domain registrations, which varies by project
  history. If you reach your project limit,
  [request additional domain quota](/docs/aistudio-custom-domains#request-additional-domains).

{% callout type="note" %}
  Attaching a Cloud Billing account upgrades a Starter Tier project to a standard
  paid Google Cloud project. After upgrading, your account is no longer eligible
  for the Google Cloud Starter Tier.

{% /callout %}

## Pricing and billing  {% id="pricing" %}

Google bills custom domain charges to the Cloud Billing account linked to your
Google Cloud project. Total cost combines the annual domain registration price
and ongoing Cloud DNS hosting fees.

| Charge | Price | Billing schedule |
| :--- | :--- | :--- |
| **Domain registration** | Starting at $12.00/year (varies by top-level domain, such as `.com`, `.net`, `.app`, or `.cloud`) | Billed upfront for 1 year. Renews annually unless canceled |
| **Cloud DNS managed zone** | Starting at $2.40/year ($0.20/month per managed zone), plus [query usage fees](https://cloud.google.com/dns/pricing) | Billed monthly based on active zones and DNS query volume |

{% callout type="warning" %}
  AI Studio creates a Cloud DNS managed zone in your Google Cloud project to route
  traffic from your domain to Cloud Run. Keep this managed zone intact while your
  custom domain is connected, or visitors will not be able to reach your app.
  Domain purchases are non-refundable once registered.

{% /callout %}

## Buy and connect a domain  {% id="buy-domain" %}

You can purchase a new domain while publishing an app for the first time, or add
one to an already published app. The following sections also cover email
verification and SSL provisioning.

1. Open your web app in [Build mode](https://aistudio.google.com/apps) and click
  **Publish** in the top-right corner.
2. Start the custom domain flow:  * **Unpublished app**: Confirm your Google Cloud project and billing account,
    click **Continue**, and click **Purchase a domain** on the **Custom
    domains** card.
  * **Published app**: Next to **App URL**, click **+** (**Add custom domain**)
    and select **Buy a new domain**. To replace a connected domain, open the
    three-dot **Custom domain options** menu and select
    **Change custom domain > Purchase a domain**.

3. Enter the domain name you want in **Search for a domain** and press **Enter**
  or click the search button. AI Studio displays available domains and their
  annual registration prices.
4. Click **Select** next to the domain you want. Click **Cost breakdown** to
  review the domain registration cost and base Cloud DNS fees.
5. Check the box acknowledging the
  [Squarespace Terms of Service](https://www.squarespace.com/terms-of-service)
  and [Google Cloud Terms](https://cloud.google.com/terms) (shown on the first
  domain purchase in a project), then click **Continue**.
6. Fill out your registrant contact details. Enter your name, email, phone
  number (for example, `+1 888 555 0123`), and mailing address. Your contact
  information is private by default and hidden from public WHOIS lookups.
7. Click **Purchase domain for `<price>`+ /year** (for example, **Purchase
  domain for $14.40+ /year**). Some Cloud Run regions don't support domain
  mappings. If needed, AI Studio asks before moving your service to a supported
  region.
8. After the confirmation banner appears, click **Continue** (and **Publish your
  app** if you are publishing for the first time) to connect the domain.

### Email verification  {% id="verify-email" %}

After purchasing a domain, you must verify your registrant email address within
**15 days** or the registrar suspends the domain. Look for an email from
`no-reply@squarespace.com` (Cloud Domains' registrar partner) and click the
verification link inside.

While verification is pending, AI Studio displays a warning icon next to your
domain in the **Publish** panel. Verification emails can take several minutes to
arrive. If you cannot find the email, click the three-dot **Custom domain
options** menu next to your domain, select **Manage subscription**, and resend
the verification email from the Google Cloud console.

### SSL certificate provisioning  {% id="ssl-provisioning" %}

After purchase, AI Studio connects your domain in three stages shown in the
status spinner next to your domain under **App URL(s)**:

1. **Purchasing domain**: Registers the domain in Cloud Domains.
2. **Connecting domain to your app**: Creates the Cloud DNS managed zone, sets
  DNS records, and maps the domain to your Cloud Run service.
3. **Provisioning SSL certificate**: Issues a Google-managed SSL certificate so
  your domain serves HTTPS traffic.

DNS and SSL setup takes 15 to 30 minutes. DNS changes can take longer to
propagate. Your app stays accessible at its `ai.studio` URL while setup
completes. If domain attachment encounters a temporary error, click **Retry**
next to the domain row.

## Reuse an owned domain  {% id="reuse-domain" %}

You can connect any domain you previously purchased through Google AI Studio in
the same Google Cloud project, whether it sits unassigned in your portfolio or
is attached to another AI Studio app.

1. Open the **Publish** panel on the target app.
2. Select **Use a domain I own** on the **Custom domains** card (or click **+**
  next to **App URL** and select **Use a domain you own** on a published app).
3. Select the domain from the list. If it's attached to another app, confirm the
  **Move domain** prompt.
4. Click **Continue**. Then click **Publish your app** (on first publish) or
  **Finish** (when replacing a domain).

AI Studio detaches moved domains from the previous app and routes traffic to the
new app. The previous app stays accessible at its `ai.studio` URL.

## Manage or cancel subscriptions  {% id="manage-domain" %}

To manage a connected custom domain, open your published app's **Publish** panel
and click the three-dot **Custom domain options** menu next to the domain under
**App URL(s)**:

* **Manage subscription**: Opens your domain registration in the
  [Cloud Domains console](https://console.cloud.google.com/net-services/domains/registrations/list).
  Use this page to edit your contact information, resend the verification email,
  inspect DNS settings, or change annual auto-renewal settings.
* **Change custom domain**: Replaces the app's custom domain by buying a new
  domain (**Purchase a domain**) or picking another domain from your project
  (**Use a domain I own**). AI Studio asks whether to keep or cancel the
  subscription for the domain being replaced.
* **Remove custom domain**: Detaches the custom domain so your app uses its
  built-in `ai.studio` URL, then prompts you to choose what happens to your
  domain billing:  * **Cancel domain subscription**: Turns off annual auto-renewal. The domain
    remains yours until its current 1-year term ends and then expires without
    renewing. Canceling doesn't delete the domain's
    [Cloud DNS managed zone](https://console.cloud.google.com/net-services/dns/zones).
    To stop the $0.20/month fee, delete that managed zone in Cloud DNS if you
    won't reuse the domain.
  * **Keep domain subscription**: Leaves annual auto-renewal active and keeps
    the domain in your project portfolio so you can attach it to another app
    later.


Unpublishing an app or deleting it from the
[Apps page](https://aistudio.google.com/apps) shows the same prompt if a custom
domain is attached. You can cancel or keep the domain subscription before the
app is unpublished or removed.

## Request additional domains  {% id="request-additional-domains" %}

Each Google Cloud project has a default **Domain registrations** quota based on
account and billing history. If you reach your limit, request a higher quota in
the Google Cloud console.

{% button href="https://console.cloud.google.com/iam-admin/quotas?service=domains.googleapis.com&metric=domain-registrations" icon="north_east" variant="secondary" %}Open domain registration quota{% /button %}

Before submitting a request, confirm your project has an active Cloud Billing
account. Your Google Account also needs `serviceusage.quotas.update` or
`cloudquotas.quotas.update`. Predefined roles with this permission include
**Owner**, **Editor**, **Cloud Quotas Admin** (`roles/cloudquotas.admin`), and
**Quota Administrator** (`roles/servicemanagement.quotaAdmin`).

To request a higher domain limit:

1. Open the
  [Domain registrations quota](https://console.cloud.google.com/iam-admin/quotas?service=domains.googleapis.com&metric=domain-registrations)
  page in the Google Cloud console.
2. In the project picker at the top of the console, select the Google Cloud
  project linked to your AI Studio app.
3. Check the box next to **Domain registrations** (under **Cloud Domains API**),
  then click **Edit** (pencil icon). If prompted, click **Apply for higher
  quota**.
4. Enter the total domains needed in **New value**, describe your use case in
  **Request description**, and click **Done**.
5. Click **Next**, confirm your contact details if prompted, and click **Submit
  request**.

Requests on newer Google Cloud projects undergo manual review and take 1 to 2
business days. Google Cloud Support emails you after reviewing your request.
Check pending requests on the
[Increase Requests tab](https://console.cloud.google.com/iam-admin/quotas/qirs).

Removing a domain from an app in AI Studio keeps the registration active until
its paid 1-year term ends. Even with **Cancel domain subscription**, the domain
counts toward your limit until it expires. To free quota earlier, transfer the
domain to another registrar and delete it in
[Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list).

## Troubleshooting  {% id="troubleshooting" %}

| Symptom | Cause and resolution |
| :--- | :--- |
| **Domain registration quota exceeded** | Your project reached its active domain registration limit. Reuse an existing domain with **Use a domain I own**, or [request additional domain quota](/docs/aistudio-custom-domains#request-additional-domains). |
| **Warning icon: email verification required** | The registrant email has not been verified yet. Open the email from `no-reply@squarespace.com`, or click **Custom domain options > Manage subscription** to resend it from Google Cloud console. |
| **Failed status with `Retry` button** | Domain setup or DNS propagation timed out. Click **Retry** next to the domain row. |
| **App asks to move to a new region** | Cloud Run domain mappings are available only in supported regions. Confirming redeploys your app to a supported region. Your `ai.studio` URL and custom domain continue working, while the underlying `run.app` service URL changes. |

## Limitations  {% id="limitations" %}

* **Domains registered outside AI Studio**: Only domains purchased in Google AI
  Studio within the same Google Cloud project appear under **Use a domain I
  own**. We plan to support transferring or connecting domains from external
  registrars in the future.
* **Web apps on paid projects only**: Custom domains work with web apps
  published on a paid Google Cloud project, not Android apps or Starter Tier
  apps.
* **Supported top-level domains and length**: Search results include only
  top-level domains that support private WHOIS protection. Domain names can be
  at most 63 characters long.
* **One custom domain per app**: Connecting a new custom domain to an app
  replaces any custom domain already attached to that app.

## What's next  {% id="whats-next" %}

* Learn more about
  [Publish your app in Google AI Studio](/docs/aistudio-deploying).
* Review [Billing](/docs/billing) for paid Google Cloud projects.
* Read the
  [Google Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/view-manage)
  for general project quota management.

