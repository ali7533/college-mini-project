from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Choice
from .forms import QuizUserCreationForm, QuizAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = QuizUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('quiz_view')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = QuizUserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = QuizAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz_view')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = QuizAuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required(login_url='login')
def quiz_view(request):
    questions = Question.objects.all()
    
    # helper for time calculation
    import time
    from .models import QuizSettings
    
    # Get dynamic duration or default to 5 minutes
    settings = QuizSettings.objects.first()
    if settings:
        QUIZ_DURATION = settings.time_limit_minutes * 60
    else:
        QUIZ_DURATION = 300 # Default fallback
    
    if 'quiz_start_time' not in request.session:
        request.session['quiz_start_time'] = time.time()
        
    start_time = request.session['quiz_start_time']
    elapsed_time = time.time() - start_time
    remaining_time = max(0, QUIZ_DURATION - elapsed_time)
    
    return render(request, 'quiz/quiz.html', {
        'questions': questions,
        'remaining_time': remaining_time
    })

@login_required(login_url='login')
def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        total = 0
        questions = Question.objects.all()
        for q in questions:
            total += 1
            selected_choice_id = request.POST.get(str(q.id))
            if selected_choice_id:
                try:
                    choice = q.choices.get(id=selected_choice_id)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass
        
        # Clear the timer session variable
        if 'quiz_start_time' in request.session:
            del request.session['quiz_start_time']
            
        return render(request, 'quiz/result.html', {'score': score, 'total': total})
    return redirect('quiz_view')
