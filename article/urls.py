from django.urls import path
from article import views

urlpatterns = [
    path('articles/',views.ArticleList.as_view()),
]
