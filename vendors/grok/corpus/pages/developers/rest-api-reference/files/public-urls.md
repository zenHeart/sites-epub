#### Files API

# Public URLs

See the [Public URLs guide](/developers/files/public-urls) for expiry behaviour, idempotency, and end-to-end examples.

***

## POST /v1/files/\{file\_id}/public-url

Create a permanent, unauthenticated public URL for an existing file. The
underlying file is unaffected and can still be fetched through the
authenticated content endpoint. Use this when you want to share a stored
asset (image, video, PDF) outside your API-keyed environment. Public URLs
can be revoked at any time via \`POST /v1/files/\{file\_id}/public-url/revoke\`.

### Path Parameters

* `file_id` (string, required) — The file's \`id\`.

### Request Body

* `expires_after` (integer | null) — Seconds from now until the public URL expires. Must be between \`3600\` (1
  hour) and \`2592000\` (30 days). Omit to inherit the file's expiry (if it
  has one) or to make the URL valid indefinitely.

### Response Body

* `expires_at` (integer | null) — Unix timestamp (seconds) when the public URL expires. Present when
  the public URL has an expiry, either from an explicit \`expires\_after\`
  in the request or inherited from the file's TTL. Absent when the
  public URL is valid indefinitely.

* `public_url` (string, required) — The full public URL.

\*\*Response example:\*\*

```json
{
  "public_url": "https://files-cdn.x.ai/ZsqeMtdcSYWPPHTQdxXDKQ/file_a128090d-f0c9-4873-bd84-e499777e7417.png",
  "expires_at": 1755600000
}
```

***

## POST /v1/files/\{file\_id}/public-url/revoke

Revoke the active public URL for a file. The underlying file remains
available through the authenticated content endpoint. Revoke is idempotent
— calling it on a file without an active public URL returns
\`revoked: false\` without an error.

### Path Parameters

* `file_id` (string, required) — The file's \`id\`.

### Response Body

* `id` (string, required) — The file ID whose public URL was revoked.

* `public_url` (string | null) — The full public URL that was revoked. Only present when \`revoked\` is \`true\`.

* `revoked` (boolean, required) — Whether a public URL was actually revoked. \`false\` if the file had no
  active public URL (no-op).

\*\*Response example:\*\*

```json
{
  "id": "file_a128090d-f0c9-4873-bd84-e499777e7417",
  "revoked": true,
  "public_url": "https://files-cdn.x.ai/ZsqeMtdcSYWPPHTQdxXDKQ/file_a128090d-f0c9-4873-bd84-e499777e7417.png"
}
```
