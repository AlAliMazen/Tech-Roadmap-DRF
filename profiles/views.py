from django.http import Http404
from django.db.models import Count
from rest_framework import generics,filters, status
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from tech_roadmap_root.permissions import IsOwnerOrReadOnly


# Create your views here.

class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view (post method),
    """
    queryset = Profile.objects.annotate(
        articles_count=Count('owner__article', distinct=True),
        # the ones who follow the profile owner
        followers_count=Count('owner__followed', distinct=True),
        
        # the ones who is being followed by the owner
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')

    # adding the filter mechanism
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_field = [
        'owner__following__followed__profile',
    ]
    ordering_fields = [
        'articles_count',
        'followers_count',
        'following_count',

        # adding on how recent and how long they have beein following or followd
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Updte and Destroy a profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        articles_count=Count('owner__article', distinct=True),
        # the ones who follow the profile owner
        followers_count=Count('owner__followed', distinct=True),
        
        # the ones who is being followed by the owner
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
   