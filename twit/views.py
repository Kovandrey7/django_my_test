from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from twit.models import Twit
from twit.serializers import TwitSerializer


class TwitViewSet(ModelViewSet):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer
