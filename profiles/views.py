from django.http import Http404
from django.db.models import Count
from rest_framework import generics,filters, status
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
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Updte and Destroy a profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
   