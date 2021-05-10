from rest_framework import serializers

from Core.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only = ["id", "time_stamp"]
