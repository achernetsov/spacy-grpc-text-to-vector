Mirror of https://gitlab.com/archertech-chipa/spacy-grpc-text-to-vector

# Overview

gRPC API for [spacy.io](spacy.io) ```nlp("some text").vector```, to transform text to vector using pretrained
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

Project includes testing script:

```shell
GRPC_DNS_RESOLVER=native TEXT_TO_VECTOR_SERVICE=text-to-vec-$LANG:50051 \
  python tester-client.py dim=300 min_similarity=0.71 "how old are you?" \
  "what is your age?"
```

Script calls server to transform 2 texts to vectors and checks that vectors are similar enough.

Script is used in CI acceptance tests.

## Building image for other NLP models

Image can be created for any available spacy [model](https://spacy.io/models):

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

### Integration (acceptance) tests

See .gitlab-ci.yml

Example:

```yaml
test-image-en:
  image: $CI_REGISTRY_IMAGE/base:latest
  stage: acceptance
  variables:
    LANG: en
  services:
    - name: $CI_REGISTRY_IMAGE/$LANG:latest
      alias: text-to-vec-en
  script:
    - |
      GRPC_DNS_RESOLVER=native TEXT_TO_VECTOR_SERVICE=text-to-vec-$LANG:50051 \
          python tester-client.py dim=300 min_similarity=0.71 "how old are you?" \
          "what is your age?"
```

# Credits
* [spacy.io](https://spacy.io)
* This project was created as part of [chipa bots](https://archertech.ru/projects/chipa/) system. 
[blog post (ru) >>](https://archertech.ru/posts/2023-03-18-chipa-text-to-vector)
