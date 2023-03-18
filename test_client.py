import asyncio
import logging

import grpc

import text_to_vector_pb2
import text_to_vector_pb2_grpc


async def run(text: str) -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = text_to_vector_pb2_grpc.TextToVectorStub(channel)
        print(f"Transforming text: {text}")
        response: text_to_vector_pb2.Vector = await stub.Transform(text_to_vector_pb2.Text(text=text))
    print(f"Vector: {response.vector}")

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        logging.error("Text should be provided as first argument")
        exit(1)

    asyncio.run(run(args[0]))
