FROM python:3.12

WORKDIR /app


RUN pip install poetry grpcio grpcio-tools


COPY pyproject.toml poetry.lock ./


RUN poetry install --no-dev


COPY . .


RUN python -m grpc_tools.protoc --python_out=./proto --grpc_python_out=./proto --proto_path=./proto proto/order.proto

CMD ["poetry", "run", "python", "src/service.py"]
