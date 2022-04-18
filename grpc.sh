#!/bin/bash

mkdir -p ./src/generated

./venv/bin/python -m grpc_tools.protoc -I. --python_out=./src/generated --grpc_python_out=./src/generated FMBService.proto