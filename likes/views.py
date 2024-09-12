from rest_framework import generics, permissions
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Like
from likes.serializers import LikeSerializer


# Create your views here.
class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    used to get specific like and be able to delete it
    """
    # check permissions that user is logged in
    permission_classes = [IsOwnerOrReadOnly]
    # get the serializer form which also enables notification
    serializer_class = LikeSerializer

    queryset = Like.objects.all()
