# Overview

gRPC API for [spacy.io](spacy.io) nlp text-to-vector function, to transform text to vector using pretrained
spacy [models](https://spacy.io/models).

For HTTP API, see [spacy fastapi](https://spacy.io/usage/projects#fastapi).

## Usage

Prerequisites:

* docker, docker-compose

### 1. Run service in docker

Repository contains docker-compose.yml with prebuild image for English language (spacy en_core_web_md model):

```shell
docker-compose up -d
```

### 2. Call service from gRPC client

Prerequisites:

* Python >= 3.10
* [Poetry](https://python-poetry.org)
* Optional: configure Poetry to install .venv locally to project: ```poetry config --local virtualenvs.in-project true```

```shell
poetry install --without dev
```

Run testing client script:

```shell
GRPC_DNS_RESOLVER=native python test_client.py "hello world!"
```

You should see vector representation of your text:

```
Transforming text: hello world
Vector: [2.3329999446868896, 1.0103850364685059,...
```

## Building image for other NLP models

Image can be created for any available spacy [model](https://spacy.io/models): 

1. Build dockerfile for required model

Example of building image for English model:

```shell
#!/bin/bash
docker build --build-arg NLP_MODEL=en_core_web_md -t imagename .
```

# <a name="development"></a> Development

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
* [spacy.io](https://spacy.io)
* This project was created as part of [chipa bots](https://archertech.ru/projects/chipa/) system.