from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from twit.views import TwitViewSet

r = DefaultRouter()
r.register("twit", TwitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls
