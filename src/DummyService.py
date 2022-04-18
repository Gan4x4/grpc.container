import generated.DummyService_pb2_grpc as rpc
import generated.DummyService_pb2 as service


from PIL import Image
import io
import os
import grpc
from os.path import dirname, abspath


import sys
import numpy as np


class DummyService(rpc.DummyServiceServicer):  # inheriting here from the protobuf rpc file which is generated

    def __init__(self):
        pass


    def preprocess(self,pil_image):

        # ImageNet
        mean = [0.485, 0.456, 0.406]
        std = [0.229, 0.224, 0.225]

        img = pil_image.resize((224, 224))
        img = np.asarray(img) / 255
        normalized = (img - mean) / (std)


    # for gRPC
    def analyzeImage(self, grpc_request, grpc_context):
        #pil_image = Image.open(io.BytesIO(grpc_request.image))
        #arr = self.preprocess(pil_image)
        description = "Hello world"
        return service.AnalyzeResponse(description=description)


