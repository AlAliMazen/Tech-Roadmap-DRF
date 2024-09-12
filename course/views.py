from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Course.objects.annotate(
        reviews_count=Count("reviews", distinct=True),
        ratings_count=Count("ratings", distinct=True),
        enrollments_count=Count("enrollments", distinct=True),
    ).order_by("-created_at")

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__profile__nickname",
        "enrollments__owner__profile__nickname",
        "ratings__owner__profile__nickname",
        "reviews__owner__profile__nickname",
    ]
    search_fields = [
        'title',
        'about',
        'owner__username',
    ]
    ordering_fields = [
        "reviews_count",
        "ratings_count",
        "enrollments_count",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseDetail(generics.RetrieveDestroyAPIView):
    """
    Only to get or delete own courses, because update is not done
    by the participant.
    """

    # set permission that logged in user can update his own comment,
    # delete it or update
    permission_classes = [IsOwnerOrReadOnly]

    # Serializer for getting the exact comment to the article
    serializer_class = CourseSerializer
    queryset = Course.objects.annotate(
        reviews_count=Count("reviews", distinct=True),
        ratings_count=Count("ratings", distinct=True),
        enrollments_count=Count("enrollments", distinct=True),
    ).order_by("-created_at")
