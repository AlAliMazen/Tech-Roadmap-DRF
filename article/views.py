from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

class ArticleList(APIView):
    """
    List all written articles
    """
    # serializer form 
    serializer_class= ArticleSerializer

    # Onyl authenticated user can write an article otherwise only read
    permission_classes=[
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(
            article, many=True, context={"request":request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(
            data = request.data, context={'request':request}
        )
        # check if the coming serializer data are valid
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        # otherwise when wrong
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
