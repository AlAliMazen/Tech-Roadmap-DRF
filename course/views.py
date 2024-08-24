from rest_framework import generics, permissions,filters, status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework.response import Response
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class CourseList(generics.ListCreateAPIView):
    """
    List all the available courses
    """
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()

    filter_backends =[
        DjangoFilterBackend
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class CourseDetail(generics.RetrieveDestroyAPIView):
    """
    Only to get or delete own courses, because update is not done
    by the participant.
    """
    # set permission that logged in user can update his own comment, delete it or update
    permission_classes = [IsOwnerOrReadOnly]

    # Serializer for getting the exact comment to the article
    serializer_class = CourseSerializer
    queryset = Course.objects.all()