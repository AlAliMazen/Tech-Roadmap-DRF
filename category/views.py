from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializer import CategorySerializer
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from django.http import Http404

# Create your views here.
class CategoryList(APIView):
    """
    created to list all available categries for the Technology areas 
    e.g. Software Developement, Networking, Cyber-Security, Virtualisation...
    """

    # serializer class for CREATE a Category
    serializer_class = CategorySerializer
    
    # check if the user is logged in and authenticated in order to write a post.
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(
            category, many=True, context={"request":request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(
            data = request.data, context={"request":request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

