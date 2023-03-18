#!/bin/bash
docker build --build-arg NLP_MODEL=en_core_web_md \
    -t registry.gitlab.com/chipa-group/chipa-nlp/text-to-vector/en:2.0.0 .