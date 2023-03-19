import asyncio
import logging

import grpc
import numpy as np
from numpy import dot
from numpy.linalg import norm
from pydantic import BaseSettings

import text_to_vector_pb2
import text_to_vector_pb2_grpc


class Settings(BaseSettings):
    text_to_vector_service: str


async def run(dimension: int, min_cos_sim: float, text1: str, text2: str) -> None:
    async with grpc.aio.insecure_channel(settings.text_to_vector_service) as channel:
        stub = text_to_vector_pb2_grpc.TextToVectorStub(channel)
        print(f"Transforming text1: {text1}")
        vec1: text_to_vector_pb2.Vector = await stub.Transform(text_to_vector_pb2.Text(text=text1))

        print(f"Transforming text2: {text2}")
        vec2: text_to_vector_pb2.Vector = await stub.Transform(text_to_vector_pb2.Text(text=text2))

    assert len(vec1.vector) == dimension
    assert len(vec2.vector) == dimension
    print(f"Correct vector dimension = {dimension}")

    # https://stackoverflow.com/a/1401828/827704
    v1 = np.array(vec1.vector)
    v2 = np.array(vec2.vector)
    cos_sim = dot(v1, v2) / (norm(v1) * norm(v2))
    print(f"cos_sim = {cos_sim}")
    assert cos_sim >= min_cos_sim
    print(f"Cosine similarity >= minimum threshold {min_cos_sim}")


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) != 4:
        logging.error("Arguments: dim=300 min_similarity=0.7 \"text1\" \"text2\"")
        exit(1)

    settings = Settings()

    dim: int = int(args[0].split("=")[1])
    print(f"Expected vector dimension = {dim}")

    similarity: float = float(args[1].split("=")[1])
    print(f"Minimum cosine similarity = {similarity}")

    txt1 = args[2]
    print(f"Text 1 = {txt1}")

    txt2 = args[3]
    print(f"Text 2 = {txt2}")

    asyncio.run(run(dim, similarity, txt1, txt2))
