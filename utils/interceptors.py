import grpc
from grpc.aio._interceptor import ClientCallDetails


class AuthInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self):
        async def abort(ignored_request, context):
            await context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")

        self._abortion = grpc.unary_unary_rpc_method_handler(abort)

    async def intercept_service(self, continuation, handler_call_details):
        meta = handler_call_details.invocation_metadata
        token = ""
        try:
            token = next(filter(lambda x: x.key == "rpc-auth", meta)).value
        except StopIteration:
            return self._abortion
        print("TOKEN", token)

        # TODO: check jwt token if incorrect - self._abortion

        if True:
            return await continuation(handler_call_details)
        else:
            return self._abortion


class KeyAuthClientInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self, secret_key):
        self.secret_key: str = secret_key

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.append(("rpc-auth", self.secret_key))
        new_details = ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
        )
        response = await continuation(new_details, request)
        return response
