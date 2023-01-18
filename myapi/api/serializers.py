from rest_framework import serializers

# models
from .models import Resume


class ResumeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Resume
    fields = ('grade','status','specialty','salary','education','experience','portfolio','title','phone','email')