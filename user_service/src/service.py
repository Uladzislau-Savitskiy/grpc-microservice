from concurrent import futures
import grpc

from microservice.user_service.proto import user_pb2

from microservice.user_service.proto import user_pb2_grpc
from database import get_db
from models import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        db = next(get_db())
        user = User(name=request.name, email=request.email, age=request.age)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user_pb2.UserResponse(user=user_pb2.User(id=user.id, name=user.name, email=user.email, age=user.age))

    def GetUser(self, request, context):
        db = next(get_db())
        user = db.query(User).filter(User.id == request.id).first()
        if user is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
        return user_pb2.UserResponse(user=user_pb2.User(id=user.id, name=user.name, email=user.email, age=user.age))

    def UpdateUser(self, request, context):
        db = next(get_db())
        user = db.query(User).filter(User.id == request.id).first()
        if user is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
        user.name = request.name
        user.email = request.email
        user.age = request.age
        db.commit()
        db.refresh(user)
        return user_pb2.UserResponse(user=user_pb2.User(id=user.id, name=user.name, email=user.email, age=user.age))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
