FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry install
RUN python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./proto/*.proto

CMD ["python", "src/service.py"]
