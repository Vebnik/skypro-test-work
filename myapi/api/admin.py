from django.contrib import admin

# models
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
  list_display = (
    'grade', 
    'status', 
    'specialty', 
    'salary', 
    'education', 
    'experience', 
    'portfolio', 
    'title', 
    'phone', 
    'email'
  )
