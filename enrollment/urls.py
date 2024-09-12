from django.urls import path
from enrollment import views

urlpatterns = [
    path('enrollments/', views.EnrollmentList.as_view()),
    path('enrollments/<int:pk>/', views.EnrollmentDetail.as_view()),
]
