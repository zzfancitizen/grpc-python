# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import myapi_pb2 as myapi__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sayHi = channel.unary_unary(
        '/myapi.Greeter/sayHi',
        request_serializer=myapi__pb2.request.SerializeToString,
        response_deserializer=myapi__pb2.reply.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sayHi(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sayHi': grpc.unary_unary_rpc_method_handler(
          servicer.sayHi,
          request_deserializer=myapi__pb2.request.FromString,
          response_serializer=myapi__pb2.reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'myapi.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
