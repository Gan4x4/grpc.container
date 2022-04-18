from concurrent import futures
import grpc

import generated.DummyService_pb2_grpc as rpc
from DummyService import DummyService

import time
class Container:

    def __init__(self, port=50051):
        self.port = port
        self.grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        rpc.add_FMBServiceServicer_to_server(DummyService(), self.grpcServer)
        self.grpcServer.add_insecure_port(f'[::]:{self.port}')
        print(f'Starting server. Listening at {self.port}...')

    def start(self, forever = False):
        self.grpcServer.start()
        print("GrpcServer started")
        if forever:
            self.grpcServer.wait_for_termination()

    def stop(self):
        self.grpcServer.stop(None)
        self.grpcServer.wait_for_termination()
        time.sleep(2)
        print("GrpcServer stopped")


server = Container()
server.start(forever=True)