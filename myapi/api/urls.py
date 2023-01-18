
from django.urls import path, include
from rest_framework import routers

# views
from .views import ResumeApiUpdate, ResumeApiList


urlpatterns = [
  path('resume/', ResumeApiList.as_view()),
  path('resume/<int:pk>/', ResumeApiUpdate.as_view()),
]