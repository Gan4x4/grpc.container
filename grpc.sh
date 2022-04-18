#!/bin/bash

python3 -m venv venv

mkdir -p ./src/generated

#./venv/bin/pip3 install --upgrade pip
./venv/bin/python3 -m ensurepip --upgrade

./venv/bin/pip3 install --no-cache-dir -r req.txt
./venv/bin/pip3 install grpcio
./venv/bin/pip3 install grpcio-tools


./venv/bin/python -m grpc_tools.protoc -I. --python_out=./src/generated --grpc_python_out=./src/generated DummyService.proto
#cd src
./venv/bin/python index.py