from django.shortcuts import render
from .models import *

# Create your views here.
def quiz_home(request):
    questions = Question.objects.all()
    return render(request, "quize.html", context={'questions' : questions})
