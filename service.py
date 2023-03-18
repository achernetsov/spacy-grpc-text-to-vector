import asyncio
import logging
import time

import grpc
import text_to_vector_pb2
import text_to_vector_pb2_grpc

import spacy

from pydantic import BaseSettings


class Settings(BaseSettings):
    port = 50051
    nlp_model: str


class TextToVector(text_to_vector_pb2_grpc.TextToVectorServicer):
    async def Transform(self, request: text_to_vector_pb2.Text, context):
        logging.debug(f'Translating: {request.text}')
        vector = nlp(request.text).vector

        return text_to_vector_pb2.Vector(vector=vector)


async def serve() -> None:
    server = grpc.aio.server()
    text_to_vector_pb2_grpc.add_TextToVectorServicer_to_server(TextToVector(), server)
    listen_addr = f'[::]:{settings.port}'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    settings = Settings()
    start_time = time.time()
    nlp = spacy.load(settings.nlp_model)
    logging.info("nlp initialized in %s sec" % (time.time() - start_time))
    asyncio.run(serve())
