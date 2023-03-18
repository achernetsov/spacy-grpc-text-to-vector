FROM registry.gitlab.com/autofaqer-group/autofaqer-nlp/text-to-vector/base:2.0.0

#build with ARG NLP_MODEL; models: https://spacy.io/usage/models
ARG NLP_MODEL
ENV NLP_MODEL=$NLP_MODEL
RUN echo "nlp model=$NLP_MODEL"
RUN python -m spacy download $NLP_MODEL

COPY text_to_vector_pb2.py ./text_to_vector_pb2.py
COPY text_to_vector_pb2_grpc.py ./text_to_vector_pb2_grpc.py
COPY service.py ./service.py

EXPOSE 50051

CMD [ "python", "service.py" ]