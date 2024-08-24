from django.urls import path
from course import views

urlpatterns= [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
]