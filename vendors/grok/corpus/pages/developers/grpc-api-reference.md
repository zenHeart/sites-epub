#### gRPC API

# Overview

The xAI gRPC API exposes the same models and services as the REST API over gRPC. The base URL for all services is `api.x.ai`, and every call must carry the header `Authorization: Bearer <your xAI API key>`.

The protobuf definitions are published in [xai-org/xai-proto](https://github.com/xai-org/xai-proto). The [xAI Python SDK](https://github.com/xai-org/xai-sdk-python) (`xai-sdk`) uses gRPC natively; install it with `pip install xai-sdk`.

## Using buf curl

Clone the proto definitions and use [buf curl](https://buf.build/docs/curl/usage) to call the API:

```bash
git clone https://github.com/xai-org/xai-proto.git
cd xai-proto
```

All `buf curl` examples in this reference assume you run from inside the cloned `xai-proto` directory.

## Services

* [Chat](/developers/grpc-api-reference/chat) — `xai_api.Chat`
* [Image](/developers/grpc-api-reference/image) — `xai_api.Image`
* [Video](/developers/grpc-api-reference/video) — `xai_api.Video`
* [Batch Management](/developers/grpc-api-reference/batches) — `xai_api.BatchMgmt`
* [Models](/developers/grpc-api-reference/models) — `xai_api.Models`
* [Auth](/developers/grpc-api-reference/auth) — `xai_api.Auth`
* [Tokenize](/developers/grpc-api-reference/tokenize) — `xai_api.Tokenize`
* [Raw Sampling](/developers/grpc-api-reference/sample) — `xai_api.Sample`
