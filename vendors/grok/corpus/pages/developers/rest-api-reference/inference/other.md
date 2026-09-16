#### Inference API

# Account

***

## GET /v1/me

Get information about the currently authenticated caller.
Works with both API keys and OAuth tokens. Returns identity, team, and ZDR status.

### Response Body

* `api_key` (object)

  * `api_key_id` (string, required) — The API key ID.

  * `blocked` (boolean, required) — Whether the API key is blocked.

  * `disabled` (boolean, required) — Whether the API key is disabled.

  * `redacted_api_key` (string, required) — The redacted API key.

* `oauth` (object)

  * `client_id` (string, required) — The OAuth client\_id of the application.

* `team_blocked` (boolean, required) — Whether the team is blocked from making API requests.

* `team_id` (string, required) — Team ID associated with the credentials.

* `user_id` (string, required) — User ID associated with the credentials.

* `zdr_status` ("no\_zdr" | "zdr" | "pii\_scrubbing", required) — Zero Data Retention status for a team.

\*\*Response example:\*\*

```json
{
  "user_id": "59fbe5f2-040b-46d5-8325-868bb8f23eb2",
  "team_id": "5ea6f6bd-7815-4b8a-9135-28b2d7ba6722",
  "zdr_status": "no_zdr",
  "team_blocked": false,
  "api_key": {
    "redacted_api_key": "xai-...b14o",
    "api_key_id": "ae1e1841-4326-4b36-a8a9-8a1a7237db11",
    "blocked": false,
    "disabled": false
  }
}
```

***

## GET /v1/api-key

Get information about an API key, including name, status, permissions and users who created or modified this key.

### Response Body

* `acls` (array\<string>, required) — A list of ACLs authorized with the API key, e.g. \`"api-key:endpoint:\*"\`, \`"api-key:model:\*"\`.

* `api_key_blocked` (boolean, required) — Indicates whether the API key is blocked.

* `api_key_disabled` (boolean, required) — Indicates whether the API key is disabled.

* `api_key_id` (string, required) — ID of the API key.

* `create_time` (string, required) — Creation time of the API key in Unix timestamp.

* `modified_by` (string, required) — User ID of the user who last modified the API key.

* `modify_time` (string, required) — Last modification time of the API key in Unix timestamp.

* `name` (string, required) — The name of the API key specified by user.

* `redacted_api_key` (string, required) — The redacted API key.

* `team_blocked` (boolean, required) — Indicates whether the team that owns the API key.

* `team_id` (string, required) — The team ID of the team that owns the API key.

* `user_id` (string, required) — User ID the API key belongs to.

\*\*Response example:\*\*

```json
{
  "redacted_api_key": "xai-...b14o",
  "user_id": "59fbe5f2-040b-46d5-8325-868bb8f23eb2",
  "name": "My API Key",
  "create_time": "2024-01-01T12:55:18.139305Z",
  "modify_time": "2024-08-28T17:20:12.343321Z",
  "modified_by": "3d38b4dc-4eb7-4785-ae26-c3fa8997ffc7",
  "team_id": "5ea6f6bd-7815-4b8a-9135-28b2d7ba6722",
  "acls": [
    "api-key:model:*",
    "api-key:endpoint:*"
  ],
  "api_key_id": "ae1e1841-4326-4b36-a8a9-8a1a7237db11",
  "team_blocked": false,
  "api_key_blocked": false,
  "api_key_disabled": false
}
```

***

## POST /v1/tokenize-text

Tokenize text with the specified model

### Request Body

* `model` (string) — The model to tokenize with.

* `text` (string) — The text content to be tokenized.

* `user` (string | null) — Optional user identifier.

### Response Body

* `token_ids` (array\<object>, required) — A list of tokens.

  * `string_token` (string, required) — The string of the token.

  * `token_bytes` (array\<integer>, required) — The bytes that constituted the token.

  * `token_id` (integer, required) — The integer representation of the token for the model.

\*\*Request example:\*\*

```json
{
  "text": "Hello world!",
  "model": "latest"
}
```

\*\*Response example:\*\*

```json
{
  "token_ids": [
    {
      "token_id": 13902,
      "string_token": "Hello",
      "token_bytes": [
        72,
        101,
        108,
        108,
        111
      ]
    },
    {
      "token_id": 1749,
      "string_token": " world",
      "token_bytes": [
        32,
        119,
        111,
        114,
        108,
        100
      ]
    },
    {
      "token_id": 161,
      "string_token": "!",
      "token_bytes": [
        33
      ]
    }
  ]
}
```
