from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Enrollment
from .serializers import EnrollmentSerializer
# Create your views here.

class EnrollmentList(generics.ListCreateAPIView):
    """
    View all registered enrollment
    and enroll in a new course
    """
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Enrollment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'owner']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnrollmentDetail(generics.RetrieveDestroyAPIView):
    """
    User can either retrive the course s/he is enrolled in
    or
    Delete the his enrollment
    """
    # set permission that logged in user can update his own comment, delete it or update
    permission_classes = [IsOwnerOrReadOnly]

    # Serializer for getting the exact comment to the article
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()