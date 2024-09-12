from django.urls import path
from rating import views

urlpatterns = [
    path('ratings/', views.RatingList.as_view()),
    path('ratings/<int:pk>/', views.RatingDetail.as_view()),
]
