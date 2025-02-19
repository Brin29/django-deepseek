# Transformar la data a JSON
from rest_framework import serializers
from .models import Programmer, Question


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'


