from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'nombre', 'correo', 'pregunta', 'fecha_envio')
        read_only_fields = ('fecha_envio', )