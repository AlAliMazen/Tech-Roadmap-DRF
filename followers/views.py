from rest_framework import generics, permissions
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    """
    used to list all follower and whom they follow
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    used to get a specific follower and destroy it
    """
     # check permissions that user is logged in
    permission_classes = [IsOwnerOrReadOnly]
    # get the serializer form which also enables notification 
    serializer_class = FollowerSerializer

    # get all follower in the model
    queryset = Follower.objects.all()
