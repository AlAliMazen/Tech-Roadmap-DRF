from rest_framework import generics, permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer

# Create your views here.
class RatingList(generics.ListCreateAPIView):
    """
    List and post a rating for a course
    as authenticated logged in user
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']  # Filter ratings by course

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    # set permission that logged in user can update his own rating,
    #  delete or update it
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer

    queryset = Rating.objects.all()
