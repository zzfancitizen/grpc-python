from concurrent import futures
import logging

import grpc
import time
import myapi_pb2
import myapi_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(myapi_pb2_grpc.GreeterServicer):

    def __init__(self):
        pass

    def sayHi(self, request, context):
        return myapi_pb2.reply(message='My reply is %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myapi_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
