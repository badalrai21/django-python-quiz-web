from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:course_id>/', views.course_details, name='course_details'),
    path('<int:course_id>/submit/', views.submit_exam, name='submit_exam'),
    path('<int:course_id>/submission/<int:submission_id>/result/', views.exam_result, name='exam_result'),
]
