from rest_framework import serializers

from twit.models import Twit


class TwitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twit
        fields = ["id", "user", "text", "created_at"]
