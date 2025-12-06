from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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


def sign_up_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        # to check that user already exists or not
        user = User.objects.get(username = username)
        if user.exists() :
            messages.error(request, "username already exists !")
            return redirect('register')
        
        # check both password is same
        if password != confirm_password :
            messages.error(request, "Password did not match !")
            return redirect('register')
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request=request, message="Register successfully !")
        login(request, user)
        return redirect('home')
    
    return render(request, "signup.html")


# for login page
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if not user.exists():
            messages.error(request, "Username doest not exists !")
            return redirect('signin')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Password did not match")
            return redirect('signin')
        else:
            login(request, user)
            return redirect('home')
        
    return render(request, "signin.html")


def logout_view(request):
    logout(request=request)
    return redirect('home')

