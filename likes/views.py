from django.shortcuts import render
from rest_framework import generics, permissions
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikesSerializer

# Create your views here.
class LikesList(generics.ListCreateAPIView):
    """
    List all the available likes on an article
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)