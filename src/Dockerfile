FROM python:3.7

RUN pip install --upgrade pip

COPY . /opt/msu.ai/

WORKDIR /opt/msu.ai/

RUN pip install --no-cache-dir -r req.txt

# For CPU version only

RUN pip install onnxruntime

RUN mv entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]