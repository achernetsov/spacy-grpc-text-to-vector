# Overview

gRPC API for [spacy.io](spacy.io) nlp text-to-vector function, to transform text to vector using pretrained
spacy [models](https://spacy.io/models).

If you need HTTP API, see [spacy fastapi](https://spacy.io/usage/projects#fastapi) 

## Usage

1. Run docker image

Repository contains docker-compose.yml with English model image.
```shell
docker-compose up -d
```

1. Transform text to vector using gRPC client

Project contains test python script:

```shell
GRPC_DNS_RESOLVER=native python test_client.py "hello world!"
```

You should receive vector representation of your text

## Building image for other NLP models

Image can be created for any available spacy [model](https://spacy.io/models): 

1. Build dockerfile for required model

```shell
#!/bin/bash
docker build --build-arg NLP_MODEL=en_core_web_md -t imagename .
```

See build-docker-en.sh script for example of building image for en_core_web_md model.

1. Bootstrap service:

docker-compose up

1. Translate text to vector using gRPC client: 

Install gprc:

```shell
pip install gprcio
```

```shell
./test_client.sh
```

# Development

Prerequisites:

* Python >= 3.10
* [Poetry](https://python-poetry.org)
* Optional: configure Poetry to install .venv locally to project: ```poetry config --local virtualenvs.in-project true```

```shell
poetry install
```

## Testing

### No unit test

Problem with unit test: NLP model should be downloaded.

### Integration test

System is tested in CI pipeline, using docker image, see .gitlab-ci.yml

# Credits