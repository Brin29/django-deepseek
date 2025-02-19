from rest_framework import viewsets
from .serializer import ProgrammerSerializer, QuestionSerializer
from .models import Programmer, Question
from openai import OpenAI

client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    # listar elementos
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer