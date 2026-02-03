import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Category, Question, Choice

def populate():
    # 1. General Knowledge
    general_cat, _ = Category.objects.get_or_create(name="General Knowledge")
    
    # Correcting field names
    q1 = Question.objects.create(text="What is the capital of France?", category=general_cat)
    Choice.objects.create(question=q1, text="Berlin", is_correct=False)
    Choice.objects.create(question=q1, text="Madrid", is_correct=False)
    Choice.objects.create(question=q1, text="Paris", is_correct=True)
    Choice.objects.create(question=q1, text="Lisbon", is_correct=False)

    q2 = Question.objects.create(text="Who wrote 'Hamlet'?", category=general_cat)
    Choice.objects.create(question=q2, text="Charles Dickens", is_correct=False)
    Choice.objects.create(question=q2, text="William Shakespeare", is_correct=True)
    Choice.objects.create(question=q2, text="J.K. Rowling", is_correct=False)
    Choice.objects.create(question=q2, text="Leo Tolstoy", is_correct=False)

    # 2. Science
    science_cat, _ = Category.objects.get_or_create(name="Science")

    q3 = Question.objects.create(text="What is the chemical symbol for Gold?", category=science_cat)
    Choice.objects.create(question=q3, text="Ag", is_correct=False)
    Choice.objects.create(question=q3, text="Au", is_correct=True)
    Choice.objects.create(question=q3, text="Fe", is_correct=False)
    Choice.objects.create(question=q3, text="Pb", is_correct=False)

    q4 = Question.objects.create(text="What planet is known as the Red Planet?", category=science_cat)
    Choice.objects.create(question=q4, text="Earth", is_correct=False)
    Choice.objects.create(question=q4, text="Mars", is_correct=True)
    Choice.objects.create(question=q4, text="Jupiter", is_correct=False)
    Choice.objects.create(question=q4, text="Venus", is_correct=False)

    # 3. Programming
    prog_cat, _ = Category.objects.get_or_create(name="Programming")

    q5 = Question.objects.create(text="Which language is used for Django?", category=prog_cat)
    Choice.objects.create(question=q5, text="Python", is_correct=True)
    Choice.objects.create(question=q5, text="Java", is_correct=False)
    Choice.objects.create(question=q5, text="C++", is_correct=False)
    Choice.objects.create(question=q5, text="Ruby", is_correct=False)

    print("Populated database with 3 Categories and 5 Questions.")

if __name__ == '__main__':
    print("Starting population script...")
    populate()
