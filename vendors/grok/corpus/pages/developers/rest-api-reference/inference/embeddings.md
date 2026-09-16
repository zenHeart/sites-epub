#### Inference API

# Embeddings

***

## POST /v1/embeddings

Create an embedding vector representation corresponding to the input text. This is the endpoint for making requests to embedding models.

### Request Body

* `dimensions` (integer | null) — The number of dimensions the resulting output embeddings should have.

* `encoding_format` (string | null) — The format to return the embeddings in. Can be either \`float\` or \`base64\`.

* `input` (object | object | object | object)

  * `String` (string, required) — A strings to be embedded. For best performance, prepend "query: " in front of query content and prepend "passage: " in front of passage/text

  * `StringArray` (array\<string>, required) — An array of strings to be embedded

  * `Ints` (array\<integer>, required) — A token in integer to be embedded

  * `IntsArray` (array\<array\<integer>>, required) — An array of tokens in integers to be embedded

* `model` (string) — ID of the model to use.

* `preview` (boolean | null) — Flag to use the new format of the API.

* `user` (string | null) — A unique identifier representing your end-user, which can help xAI to monitor and detect abuse.

### Response Body

* `data` (array\<object>, required) — A list of embedding objects.

  * `embedding` (string | array\<number>, required)

  * `index` (integer, required) — Index of the embedding object in the data list.

  * `object` (string, required) — The object type, which is always \`"embedding"\`.

* `model` (string, required) — Model ID used to create embedding.

* `object` (string, required) — The object type of \`data\` field, which is always \`"list"\`.

* `usage` (object)

  * `prompt_tokens` (integer, required) — Prompt token used.

  * `total_tokens` (integer, required) — Total token used.

\*\*Request example:\*\*

```json
"{\n            \"input\": [\"This is an example content to embed...\"],\n            \"model\": \"v1\",\n            \"encoding_format\": \"float\"\n        }"
```

\*\*Response example:\*\*

```json
{
  "object": "list",
  "model": "v1",
  "data": [
    {
      "index": 0,
      "embedding": [
        0.01567895,
        0.063257694,
        0.045925662
      ],
      "object": "embedding"
    }
  ],
  "usage": {
    "prompt_tokens": 1,
    "total_tokens": 1
  }
}
```

***

## GET /v1/embedding-models

List all embedding models available to the authenticating API key with full information. Additional information compared to /v1/models includes modalities, fingerprint and alias(es).

### Response Body

* `models` (array\<object>, required) — Array of available embedding models.

  * `aliases` (array\<string>, required) — Alias ID(s) of the model that user can use in a request's model field.

  * `created` (integer, required) — Model creation time in Unix timestamp.

  * `fingerprint` (string, required) — Fingerprint of the xAI system configuration hosting the model.

  * `id` (string, required) — Model ID. Obtainable from \<https://console.x.ai/team/default/models> or \<https://docs.x.ai/docs/models>.

  * `input_modalities` (array\<string>, required) — The input modalities supported by the model.

  * `object` (string, required) — Object type, should be model.

  * `output_modalities` (array\<string>, required) — The output modalities supported by the model.

  * `owned_by` (string, required) — Owner of the model.

  * `prompt_image_token_price` (integer, required) — Price of the prompt image token in USD cents per million token.

  * `prompt_text_token_price` (integer, required) — Price of the prompt text token in USD cents per million token.

  * `version` (string, required) — Version of the model.

\*\*Response example:\*\*

```json
{
  "models": [
    {
      "id": "v1",
      "fingerprint": "fp_df37966059",
      "created": 1725148800,
      "object": "model",
      "owned_by": "xai",
      "version": "0.1.0",
      "input_modalities": [
        "text"
      ],
      "prompt_text_token_price": 100,
      "prompt_image_token_price": 0,
      "aliases": []
    }
  ]
}
```

***

## GET /v1/embedding-models/\{model\_id}

Get full information about an embedding model with its model\_id.

### Path Parameters

* `model_id` (string, required) — ID of the model to get.

### Response Body

* `aliases` (array\<string>, required) — Alias ID(s) of the model that user can use in a request's model field.

* `created` (integer, required) — Model creation time in Unix timestamp.

* `fingerprint` (string, required) — Fingerprint of the xAI system configuration hosting the model.

* `id` (string, required) — Model ID. Obtainable from \<https://console.x.ai/team/default/models> or \<https://docs.x.ai/docs/models>.

* `input_modalities` (array\<string>, required) — The input modalities supported by the model.

* `object` (string, required) — Object type, should be model.

* `output_modalities` (array\<string>, required) — The output modalities supported by the model.

* `owned_by` (string, required) — Owner of the model.

* `prompt_image_token_price` (integer, required) — Price of the prompt image token in USD cents per million token.

* `prompt_text_token_price` (integer, required) — Price of the prompt text token in USD cents per million token.

* `version` (string, required) — Version of the model.

\*\*Response example:\*\*

```json
{
  "id": "v1",
  "created": 1725148800,
  "object": "model",
  "owned_by": "xai",
  "version": "0.1.0",
  "input_modalities": [
    "text"
  ],
  "prompt_text_token_price": 10,
  "prompt_image_token_price": 0,
  "aliases": []
}
```
