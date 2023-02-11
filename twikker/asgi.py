import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twikker.settings')
import django
django.setup()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import apps.conversation.routing as conversation_routing

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            conversation_routing.websocket_urlpatterns
        )
    )
})
