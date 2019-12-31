import grpc
from src.ComputeService_pb2_grpc import ComputeServiceStub
from src.ComputeService_pb2 import areaOfRectangleRequest


def run():
    host = "127.0.0.1"
    port = "50051"
    channel = grpc.insecure_channel('{0}:{1}'.format(host, port))
    compute_service_stub = ComputeServiceStub(channel)
    request = areaOfRectangleRequest(x=1, y=2)
    response = compute_service_stub.areaOfRectangle(request)
    assert response.z == 2


if __name__ == '__main__':
    run()
