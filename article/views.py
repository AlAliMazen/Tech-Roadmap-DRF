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
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(
            article, many=True, context={"request":request}
        )
        return Response(serializer.data)
