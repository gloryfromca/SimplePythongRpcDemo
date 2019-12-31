import grpc
from src.ComputeService_pb2_grpc import ComputeServiceStub
from src.ComputeService_pb2 import areaOfRectangleRequest


def run():
    host = "127.0.0.1"
    port = "50051"
    channel = grpc.insecure_channel('{0}:{1}'.format(host, port))
    compute_service_stub = ComputeServiceStub(channel)

    result = []
    requests = []
    for i in range(0, 10):
        result.append(i * (i+1))
        requests.append(areaOfRectangleRequest(x=i, y=i+1))

    responses = compute_service_stub.areaOfRectangle(iter(requests))

    for index, response in enumerate(responses):
        assert response.z == result[index]
    print("done")


if __name__ == '__main__':
    run()
