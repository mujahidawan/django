from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter(
    {
        #"http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)