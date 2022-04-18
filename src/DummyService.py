import generated.DummyService_pb2_grpc as rpc
import generated.DummyService_pb2 as service

import onnxruntime
from PIL import Image
import io
import numpy as np


class DummyService(rpc.DummyServiceServicer):  # inheriting here from the protobuf rpc file which is generated

    def __init__(self):
        self.session = onnxruntime.InferenceSession("model.onnx")


    def preprocess(self,pil_image):

        # ImageNet normalization
        mean = [0.485, 0.456, 0.406]
        std = [0.229, 0.224, 0.225]
        img = pil_image.resize((224, 224))

        img = np.asarray(img) / 255
        normalized = (img - mean) / (std)


        # Conver to array
        out = np.transpose(normalized, axes=(2, 0, 1)) # HWC -> CHW
        out = out.astype(np.float32)  # ensure input in float32
        out = out[np.newaxis, ...]  # add batch dim

        return out


    # for gRPC
    def analyzeImage(self, grpc_request, grpc_context):
        pil_image = Image.open(io.BytesIO(grpc_request.image))
        arr = self.preprocess(pil_image)

        # call model
        first_input_name = self.session.get_inputs()[0].name
        outputs = self.session.run([], {first_input_name: arr})

        # postprocess
        class_num = int(outputs[0].argmax())
        description = str(class_num)
        return service.AnalyzeResponse(description=description)


