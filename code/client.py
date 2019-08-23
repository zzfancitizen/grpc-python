from __future__ import print_function
import logging

import grpc

import myapi_pb2
import myapi_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = myapi_pb2_grpc.GreeterStub(channel)
        response = stub.sayHi(myapi_pb2.request(name='HelloWorld'))
        print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
