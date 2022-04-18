import generated.DummyService_pb2_grpc as rpc
import generated.DummyService_pb2 as service



class DummyService(rpc.DummyServiceServicer):  # inheriting here from the protobuf rpc file which is generated

    def __init__(self):
        pass


    # for gRPC
    def analyzeImage(self, grpc_request, grpc_context):
        description = "Hello world!"
        return service.AnalyzeResponse(description=description)


