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
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(
            category, many=True, context={"request":request}
        )
        return Response(serializer.data)

