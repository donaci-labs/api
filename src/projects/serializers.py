
from rest_framework import serializers
from .models import Project, ProjectImage



class ProjectImage(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('image',)


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImage(many=True)
    class Meta:
        exclude = ('published',)
        model = Project

