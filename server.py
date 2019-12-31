import time
import grpc
from src.ComputeService_pb2_grpc import add_ComputeServiceServicer_to_server, ComputeServiceServicer
from concurrent import futures


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ComputeServiceServicer_to_server(ComputeServiceServicer(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        time.sleep(26 * 60 * 60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
