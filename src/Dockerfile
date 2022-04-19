FROM python:3.7

RUN pip install --upgrade pip

COPY . /opt/dummy/

WORKDIR /opt/dummy/

RUN pip install --no-cache-dir -r req.txt

# For CPU version only

RUN pip install onnxruntime

RUN mv entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]