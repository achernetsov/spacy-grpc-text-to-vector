FROM registry.gitlab.com/archertech-chipa/spacy-grpc-text-to-vector/base

# models: https://spacy.io/usage/models
ARG NLP_MODEL
ENV NLP_MODEL=$NLP_MODEL
RUN echo "Downloading nlp model=$NLP_MODEL"
RUN python -m spacy download $NLP_MODEL

COPY service.py ./service.py

EXPOSE 50051

CMD [ "python", "service.py" ]