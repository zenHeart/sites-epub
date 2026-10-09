> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics API

> Ingest user analytics data directly into your existing analytics platform

## Overview

The Zencoder Analytics API enables programmatic access to your organization's usage data, allowing you to integrate Zencoder metrics into your existing business intelligence tools, custom dashboards, and reporting systems. This REST API provides the same data available in the [Analytics Dashboard](/features/analytics) in a machine-readable format.

<Note>
  API access is available for users on [Pro Plus plans and above](/faq/pricing). Requires **Owner or Manager** role permissions within your organization.
</Note>

## Getting Your API Credentials

Before making API requests, you'll need to generate a personal access token to obtain your `client_id` and `client_secret`:

1. Navigate to [auth.zencoder.ai](https://auth.zencoder.ai) and sign in
2. Go to **Administration → API Keys**
3. Click **Add**
4. Give API key a desired name
5. Copy the API Key, **it will only be showed once**

<Warning>
  **Important**: After generation, immediately copy and securely store **API Key**. The API Key will only be displayed once and cannot be retrieved later. Store it in a secure location such as a password manager or secrets management system.
</Warning>

Include the obtained API Key in the `zencoder-api-key` header of subsequent API requests:

```http theme={"system"}
zencoder-api-key: zak_live_pM...
```

**Example Requests**

<Tabs>
  <Tab title="cURL">
    ```bash theme={"system"}
    curl -X GET https://api.zencoder.ai/api/v1/data/usage \
      -H "zencoder-api-key: YOUR_API_KEY"
    ```
  </Tab>

  <Tab title="Node.js">
    ```javascript theme={"system"}
    // Use the token in subsequent requests
    const usageResponse = await fetch('https://api.zencoder.ai/api/v1/data/usage', {
      headers: {
        'zencoder-api-key': `YOUR_API_KEY`
      }
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"system"}
    import requests

    # Use the token in subsequent requests
    usage_response = requests.get(
        'https://api.zencoder.ai/api/v1/data/usage',
        headers={'zencoder-api-key': 'YOUR_API_KEY'}
    )
    ```
  </Tab>
</Tabs>

## Usage Data Endpoint

**Query String Parameters**

| Parameter | Type | Required | Description |
| - | - | - | - |
| `period` | string | No | Time period for usage data. Must be one of: `7d`, `30d`, `90d`. Defaults to `7d` if neither `period` nor `day` is provided |
| `day` | string | No | Specific day for usage data in `YYYY-MM-DD` format. Cannot be used together with `period` |

**Note**: You must provide either `period` OR `day`, but not both. If neither is provided, defaults to `period=7d`.

**Example Requests**

Get usage data for the last 30 days:

```http theme={"system"}
GET /api/v1/data/usage?period=30d HTTP/1.1
Host: api.zencoder.ai
zencoder-api-key: zak_live_pM...
```

Get usage data for a specific day:

```http theme={"system"}
GET /api/v1/data/usage?day=2025-10-15 HTTP/1.1
Host: api.zencoder.ai
zencoder-api-key: zak_live_pM...
```

**Response**

Success Response (200 OK):

```json theme={"system"}
{
  "status": "success",
  "data": {
    "period": {
      "start": "2025-09-24",
      "end": "2025-10-01",
      "days": 7
    },
    "summary": {
      "total_active_users": 48,
      "total_messages": 1372
    },
    "users": [
      {
        "email": "joe.doe@example.ai",
        "messages": 58,
        "last_active": "2025-10-01",
        "ides": [
          "VS Code"
        ],
        "languages": [
          "JavaScript",
          "TypeScript"
        ]
      }
    ],
    "daily": [
      {
        "day": "2025-09-24",
        "active_users": 21,
        "messages": 188,
        "ides": [
          {
            "ide_name": "VS Code",
            "engaged_users": 6
          },
          {
            "ide_name": "IntelliJ CE",
            "engaged_users": 1
          },
          {
            "ide_name": "WebStorm",
            "engaged_users": 1
          }
        ],
        "languages": [
          {
            "language_name": "JavaScript",
            "engaged_users": 1
          },
          {
            "language_name": "TypeScript",
            "engaged_users": 2
          }
        ]
      }
    ]
  }
}
```

Error Responses:

<AccordionGroup>
  <Accordion title="400 Bad Request - Invalid period parameter">
    ```json theme={"system"}
    {
      "status": "error",
      "message": "Invalid period parameter. Period has to be one of 7d, 30d, 90d"
    }
    ```
  </Accordion>

  <Accordion title="400 Bad Request - Invalid day parameter format">
    ```json theme={"system"}
    {
      "status": "error",
      "message": "Invalid day parameter. Day must be in YYYY-MM-DD format"
    }
    ```
  </Accordion>

  <Accordion title="400 Bad Request - Both period and day parameters provided">
    ```json theme={"system"}
    {
      "status": "error",
      "message": "Only one parameter is expected. Provide either 'day' or 'period', not both"
    }
    ```
  </Accordion>

  <Accordion title="500 Internal Server Error">
    ```json theme={"system"}
    {
      "status": "error",
      "message": "Failed to fetch data"
    }
    ```
  </Accordion>
</AccordionGroup>

**Response Fields**

<AccordionGroup>
  <Accordion title="Data Object">
    | Field | Type | Description |
    | - | - | - |
    | `period` | object | Time period information for the data |
    | `summary` | object | Aggregate statistics for the period |
    | `users` | array | List of user usage details |
    | `daily` | array | Daily breakdown of usage statistics |
  </Accordion>

  <Accordion title="Period Object">
    | Field | Type | Description |
    | - | - | - |
    | `start` | string | Start date of the period (ISO 8601 format) |
    | `end` | string | End date of the period (ISO 8601 format) |
    | `days` | int | Number of days in the period |
  </Accordion>

  <Accordion title="Summary Object">
    | Field | Type | Description |
    | - | - | - |
    | `total_active_users` | int | Total number of active users in the period |
    | `total_messages` | int | Total number of messages sent in the period |
  </Accordion>

  <Accordion title="User Object">
    | Field | Type | Description |
    | - | - | - |
    | `email` | string | User's email address |
    | `messages` | int | Number of messages sent by the user |
    | `last_active` | string | Date of user's last activity (ISO 8601 format) |
    | `ides` | array | List of IDEs used by the user |
    | `languages` | array | List of programming languages used |
  </Accordion>

  <Accordion title="Daily Data Object">
    | Field | Type | Description |
    | - | - | - |
    | `day` | string | Date for this data point (ISO 8601 format) |
    | `active_users` | int | Number of active users on this day |
    | `messages` | int | Number of messages sent on this day |
    | `ides` | array | IDE usage breakdown for this day |
    | `languages` | array | Language usage breakdown for this day |
  </Accordion>

  <Accordion title="IDE Usage Object">
    | Field | Type | Description |
    | - | - | - |
    | `ide_name` | string | Name of the IDE |
    | `engaged_users` | int | Number of users who used this IDE |
  </Accordion>

  <Accordion title="Language Usage Object">
    | Field | Type | Description |
    | - | - | - |
    | `language_name` | string | Name of the programming language |
    | `engaged_users` | int | Number of users who used this language |
  </Accordion>
</AccordionGroup>

**Example Requests**

<Tabs>
  <Tab title="Last 30 Days">
    <Tabs>
      <Tab title="cURL">
        ```bash theme={"system"}
        curl -X GET "https://api.zencoder.ai/api/v1/data/usage?period=30d" \
          -H "zencoder-api-key: API_KEY"
        ```
      </Tab>

      <Tab title="Node.js">
        ```javascript theme={"system"}
        const response = await fetch('https://api.zencoder.ai/api/v1/data/usage?period=30d', {
          headers: {
            'zencoder-api-key': 'API_KEY'
          }
        });
        const data = await response.json();
        ```
      </Tab>

      <Tab title="Python">
        ```python theme={"system"}
        response = requests.get(
            'https://api.zencoder.ai/api/v1/data/usage?period=30d',
            headers={'zencoder-api-key': 'API_KEY'}
        )
        data = response.json()
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Specific Day">
    <Tabs>
      <Tab title="cURL">
        ```bash theme={"system"}
        curl -X GET "https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15" \
          -H "zencoder-api-key: API_KEY"
        ```
      </Tab>

      <Tab title="Node.js">
        ```javascript theme={"system"}
        const response = await fetch('https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15', {
          headers: {
            'zencoder-api-key': 'API_KEY'
          }
        });
        const data = await response.json();
        ```
      </Tab>

      <Tab title="Python">
        ```python theme={"system"}
        response = requests.get(
            'https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15',
            headers={'zencoder-api-key': 'API_KEY'}
        )
        data = response.json()
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Last 7 Days (Default)">
    <Tabs>
      <Tab title="cURL">
        ```bash theme={"system"}
        curl -X GET "https://api.zencoder.ai/api/v1/data/usage" \
          -H "zencoder-api-key: API_KEY"
        ```
      </Tab>

      <Tab title="Node.js">
        ```javascript theme={"system"}
        const response = await fetch('https://api.zencoder.ai/api/v1/data/usage', {
          headers: {
            'zencoder-api-key': 'API_KEY'
          }
        });
        const data = await response.json();
        ```
      </Tab>

      <Tab title="Python">
        ```python theme={"system"}
        response = requests.get(
            'https://api.zencoder.ai/api/v1/data/usage',
            headers={'zencoder-api-key': 'API_KEY'}
        )
        data = response.json()
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Authentication Failures">
    * Verify your `API Key` is correct
    * Ensure your subscription is Core or higher
    * Check that your account has Owner or Manager permissions
    * Confirm you generated an API Key in Settings
  </Accordion>

  <Accordion title="Empty or Missing Data">
    * Confirm users in your organization have been active during the requested period
    * Verify the date format for `day` parameter is `YYYY-MM-DD`
    * Check that the requested date range contains activity
    * Ensure users are part of your organization and have authenticated at least once
  </Accordion>

  <Accordion title="Invalid Parameter Errors">
    * For `period` parameter, use only: `7d`, `30d`, or `90d`
    * For `day` parameter, use format: `YYYY-MM-DD`
    * Do not provide both `period` and `day` parameters in the same request
  </Accordion>

  <Accordion title="Connection or Network Issues">
    * Verify you can reach `https://fe.zencoder.ai` and `https://api.zencoder.ai`
    * Check your firewall or proxy settings
    * Ensure your network allows HTTPS requests to Zencoder endpoints
  </Accordion>
</AccordionGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.