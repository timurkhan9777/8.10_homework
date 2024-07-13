from django.shortcuts import render
from .models import UserVideo
from .serializers import UserVideoSerializer

from rest_framework.viewsets import ModelViewSet

class UserVideoAPIView(ModelViewSet):
    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer