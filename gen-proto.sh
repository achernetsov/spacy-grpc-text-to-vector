python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. \
  ./protos/text_to_vector.proto