# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import observer_pb2 as protos_dot_observer__pb2


class ObserverServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEvent = channel.unary_unary(
                '/observer.ObserverService/CreateEvent',
                request_serializer=protos_dot_observer__pb2.CreateEventRequest.SerializeToString,
                response_deserializer=protos_dot_observer__pb2.CreateEventResponse.FromString,
                )
        self.ReadEvent = channel.unary_unary(
                '/observer.ObserverService/ReadEvent',
                request_serializer=protos_dot_observer__pb2.ReadEventRequest.SerializeToString,
                response_deserializer=protos_dot_observer__pb2.ReadEventResponse.FromString,
                )
        self.UpdateEvent = channel.unary_unary(
                '/observer.ObserverService/UpdateEvent',
                request_serializer=protos_dot_observer__pb2.UpdateEventRequest.SerializeToString,
                response_deserializer=protos_dot_observer__pb2.UpdateEventResponse.FromString,
                )
        self.DeleteEvent = channel.unary_unary(
                '/observer.ObserverService/DeleteEvent',
                request_serializer=protos_dot_observer__pb2.DeleteEventRequest.SerializeToString,
                response_deserializer=protos_dot_observer__pb2.DeleteEventResponse.FromString,
                )
        self.ListEvents = channel.unary_unary(
                '/observer.ObserverService/ListEvents',
                request_serializer=protos_dot_observer__pb2.ListEventsRequest.SerializeToString,
                response_deserializer=protos_dot_observer__pb2.ListEventsResponse.FromString,
                )


class ObserverServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObserverServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEvent,
                    request_deserializer=protos_dot_observer__pb2.CreateEventRequest.FromString,
                    response_serializer=protos_dot_observer__pb2.CreateEventResponse.SerializeToString,
            ),
            'ReadEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadEvent,
                    request_deserializer=protos_dot_observer__pb2.ReadEventRequest.FromString,
                    response_serializer=protos_dot_observer__pb2.ReadEventResponse.SerializeToString,
            ),
            'UpdateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEvent,
                    request_deserializer=protos_dot_observer__pb2.UpdateEventRequest.FromString,
                    response_serializer=protos_dot_observer__pb2.UpdateEventResponse.SerializeToString,
            ),
            'DeleteEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEvent,
                    request_deserializer=protos_dot_observer__pb2.DeleteEventRequest.FromString,
                    response_serializer=protos_dot_observer__pb2.DeleteEventResponse.SerializeToString,
            ),
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=protos_dot_observer__pb2.ListEventsRequest.FromString,
                    response_serializer=protos_dot_observer__pb2.ListEventsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'observer.ObserverService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObserverService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/observer.ObserverService/CreateEvent',
            protos_dot_observer__pb2.CreateEventRequest.SerializeToString,
            protos_dot_observer__pb2.CreateEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/observer.ObserverService/ReadEvent',
            protos_dot_observer__pb2.ReadEventRequest.SerializeToString,
            protos_dot_observer__pb2.ReadEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/observer.ObserverService/UpdateEvent',
            protos_dot_observer__pb2.UpdateEventRequest.SerializeToString,
            protos_dot_observer__pb2.UpdateEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/observer.ObserverService/DeleteEvent',
            protos_dot_observer__pb2.DeleteEventRequest.SerializeToString,
            protos_dot_observer__pb2.DeleteEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/observer.ObserverService/ListEvents',
            protos_dot_observer__pb2.ListEventsRequest.SerializeToString,
            protos_dot_observer__pb2.ListEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
