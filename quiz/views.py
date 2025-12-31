from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Question

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('quiz_view')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

def login_user(request,):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('quiz_view')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

def quiz_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        total = 0
        questions = Question.objects.all()
        for q in questions:
            total += 1
            selected_choice_id = request.POST.get(str(q.id))
            if selected_choice_id:
                choice = q.choices.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': total})
    return redirect('quiz_view')
