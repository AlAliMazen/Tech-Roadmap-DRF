from django.http import Http404
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from tech_roadmap_root.permissions import IsOwnerOrReadOnly


# Create your views here.

class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request':request}
            )
        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    used to get the profile details
    """
    # following is used to create a form from the profile class in the model 
    serializer_class = ProfileSerializer

    # check the permission of the each profile
    permission_classes =[IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile =self.get_object(pk)
        # because we only want one single profile we don't pass the many arg
        serializer = ProfileSerializer(profile, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)