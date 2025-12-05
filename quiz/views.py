from django.shortcuts import render
from .models import *

# Create your views here.
def quiz_home(request):
    questions = Question.objects.all()

    if request.method == "POST":
        score = 0
        total = questions.count()

        for q in questions:
            selected_id = request.POST.get(str(q.id))
            if selected_id:
                answer = Answer.objects.get(id = selected_id)
                if answer.is_true:
                    score+=1
        
        return render(request, "result.html", context={'score':score, 'total':total})


    return render(request, "quize.html", context={'questions' : questions})
