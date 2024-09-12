from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


# Create your views here.
class ReviewList(generics.ListCreateAPIView):
    """
    List and create all the reviews
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'owner']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # set permission that logged in user can update his own comment,
    # delete it or update
    permission_classes = [IsOwnerOrReadOnly]

    # Serializer for getting the exact comment to the article
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
