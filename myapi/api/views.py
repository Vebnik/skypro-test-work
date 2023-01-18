from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from rest_framework.generics import UpdateAPIView, ListAPIView
import json

# models
from .models import Resume
from .serializers import ResumeSerializer


class ResumeApiUpdate(LoginRequiredMixin, UpdateAPIView):
  login_url = '/'
  redirect_field_name = 'redirect_to'

  queryset = Resume.objects.all()
  serializer_class = ResumeSerializer

  def partial_update(self, request, *args, **kwargs):
    return super().partial_update(request, *args, **kwargs)


class ResumeApiList(ListAPIView):
  queryset = Resume.objects.all()
  serializer_class = ResumeSerializer
