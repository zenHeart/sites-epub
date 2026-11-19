> ## AI Agent Context
> Get the complete documentation index at: https://aistudio.google.com/llms.txt
> Use this file to discover all available pages.
> For the full documentation in a single file, fetch: https://aistudio.google.com/llms-full.txt

# Troubleshoot Google AI Studio

This page provides suggestions for troubleshooting Google AI Studio if you
encounter issues.

## Understand 403 Access Restricted errors  {% id="understand-403-errors" %}

If you see a 403 Access Restricted error, you are using Google AI Studio in a
way that does not follow the [Terms of Service](/docs/terms). One common reason is
you are not located in a [supported region](/docs/available-regions).

## Verify age requirements for your Google Account  {% id="age-requirements" %}

You must be 18 or older to use Google AI Studio. You may be redirected to this
section while trying to open [Google AI Studio](https://aistudio.google.com/).
If so, verify that your Google Account meets the age requirement:

* **Check your birthday:** Confirm your date of birth is set to 18 or older in
  your [birthday settings](https://myaccount.google.com/birthday).
* **Verify your age:** Complete
  [age verification](https://myaccount.google.com/age-verification) on your
  Google Account. For verification options, see
  [Verify your age on your Google Account](https://support.google.com/accounts/answer/10071085).
* **Match your ID date of birth:** If you verify your age with an ID, check your
  account settings. Make sure your
  [birthday](https://myaccount.google.com/birthday) matches the date on your ID.
* **Google Workspace accounts:** For Google Workspace for Education accounts,
  contact your administrator. They can confirm if your account is designated as
  18 or older. See
  [Access Google AI Studio with your Workspace account](/docs/workspace) for
  details.

## Resolve No Content responses on Google AI Studio  {% id="resolve-no-content" %}

{% callout type="warning" %}
  A **No Content** message appears on Google AI Studio if the content is blocked
  for any reason. To see more details, hold the pointer over **No Content** and
  click **Safety**.

{% /callout %}

If the response was blocked due to [safety settings](/docs/safety-settings) and
you considered the [safety risks](/docs/safety-guidance) for your use case, you
can modify the
[safety settings](/docs/safety-settings#safety-settings-ai-studio)
to influence the returned response.

If the response was blocked but not due to the safety settings, the query or
response may violate the [Terms of Service](/docs/terms) or be otherwise unsupported.

## Check token usage and limits  {% id="check-token-usage" %}

When you have a prompt open, the **Text Preview** button at the bottom of the
screen shows the current tokens used for the content of your prompt and the
maximum token count for the model being used.

## Google Cloud IAM permissions for AI Studio  {% id="iam-permissions" %}

Members of a Google Cloud project need specific Identity and Access Management
(IAM) permissions to perform actions in Google AI Studio. For more information
about these identities, see the
[IAM principals overview](https://docs.cloud.google.com/iam/docs/principals-overview).

Users with the **Editor** or **Owner** roles in the associated Google Cloud
project have full permissions to view dashboards and manage Gemini API keys.
Users with the **Viewer** role can view dashboards and API keys, but cannot
create, update, or delete them.

For more granular control, refer to the following table for the specific
permissions required for each AI Studio feature. For instructions on how to
grant these permissions, see
[Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
in the Google Cloud documentation.

{% table %}
  * AI Studio feature
  * Required IAM permissions
  * Additional requirements

  ---

  * **Search project** (import projects)
  * `resourcemanager.projects.get`
  * &nbsp;

  ---

  * **Rename project**
  * `resourcemanager.projects.update`
  * &nbsp;

  ---

  * **Display quota tier**
  * N/A
  * &nbsp;

  ---

  * **Create API key**
  *     Have **Search project** permissions, and:

    `apikeys.keys.create`

    `serviceusage.services.enable`

    `iam.serviceAccountApiKeyBindings.create`

    `iam.serviceAccounts.create`

  * 

  ---

  * **List API keys**
  *     Have **Search project** permissions, and:

    `apikeys.keys.list`

    `serviceusage.services.get`

  * The Google Cloud project must have the [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com) enabled.

  ---

  * **Rename API keys**
  * `apikeys.keys.update`
  * &nbsp;

  ---

  * **Delete API keys**
  * `apikeys.keys.delete`
  * &nbsp;

  ---

  * **Usage dashboard**
  *     Have **Search project** permissions, and:

    `monitoring.timeSeries.list`

  * &nbsp;

  ---

  * **Rate limit dashboard**
  *     Have **Usage dashboard** permissions, and:

    `cloudquotas.quotas.get`

  * &nbsp;

  ---

  * **Spend (Billing cap)**
  *     `billing.resourceCosts.get` (to view spend)

    `billing.resourcebudgets.read` (to view cap)

    `billing.resourcebudgets.write` (to set cap)

  * &nbsp;

  ---

  * **Billing dashboard**
  * `billing.accounts.get`
  * &nbsp;
{% /table %}

### Other access checks  {% id="other-access-checks" %}

In addition to Google Cloud IAM permissions, AI Studio also performs security
and compliance checks. You might encounter a `PERMISSION_DENIED` or access
restriction error in the AI Studio interface or in API responses if you do not
meet the following requirements:

* **Security checks:** Your request must pass automated security checks.
* **Terms of Service:** You must accept the Google Terms of Service and
  Generative AI Additional Terms of Service.
* **Supported region:** You must be located in a
  [supported region](/docs/available-regions).
* **Age requirements:** You must meet the
  [age requirements](/docs/troubleshoot-ai-studio#age-requirements) (18+) on
  your Google Account.
* **Trust & Safety:** The Google Cloud project must not be flagged for abuse.

