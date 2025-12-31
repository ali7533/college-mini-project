import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from quiz.models import Question, Choice

def verify():
    print("Starting verification...")
    
    # 1. Clean up previous test data
    Question.objects.all().delete()
    User.objects.filter(username='testuser').delete()
    print("Cleaned up old data.")

    # 2. Add a Question
    q = Question.objects.create(text="What is the capital of France?")
    c1 = Choice.objects.create(question=q, text="Berlin", is_correct=False)
    c2 = Choice.objects.create(question=q, text="Paris", is_correct=True)
    c3 = Choice.objects.create(question=q, text="Madrid", is_correct=False)
    print(f"Created Question: {q.text}")

    # 3. Create a User
    user = User.objects.create_user('testuser', 'test@example.com', 'password123')
    print(f"Created User: {user.username}")

    # 4. Simulate Quiz Submission
    c = Client()
    login_success = c.login(username='testuser', password='password123')
    if login_success:
        print("Login successful.")
    else:
        print("Login failed!")
        return

    # Submit correct answer
    response = c.post('/submit/', {str(q.id): c2.id})
    
    if response.status_code == 200:
        # Check context for score using standard test client capabilities
        # Note: In a real browser test we'd check HTML, but here we can check the context if available
        # or just parse the content for "1 / 1"
        content = response.content.decode('utf-8')
        if "1 <span class=\"text-2xl text-gray-400 font-normal\">/ 1</span>" in content:
             print("SUCCESS: Quiz submission scored correctly (1/1).")
        else:
             print("FAILURE: Score not found in response.")
             print(content)
    else:
        print(f"FAILURE: Submit returned status code {response.status_code}")

if __name__ == '__main__':
    verify()
