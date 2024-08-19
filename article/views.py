from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from tech_roadmap_root.permissions import IsOwnerOrReadOnly

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


class ArticleDetail(APIView):
    """
    Used to update an article and delete it 
    """
    # to have a nice form we just need the serilaizer profile instance
    serializer_class = ArticleSerializer

    # only the one who wrote the article can update it 
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            self.check_object_permissions(self.request,article)
            return article
        except Article.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer=ArticleSerializer(
            article, context={'request':request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(
            article, data=request.data, context={'request':request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            article = Article.object.get(pk=pk)
            if article.owner != request.user:
                return Response({'Detail':"You don't have permission to delete this article"},
                                status=status.HTTP_403_FORBIDDEN)
            article.delete()
            return Response({'Detail':"Article deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response({'Detail':'Article not found'}, status=status.HTTP_404_NOT_FOUND)
