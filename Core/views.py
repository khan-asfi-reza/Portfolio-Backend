from rest_framework.generics import CreateAPIView
from Core.serializers import MessageSerializer


class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer
