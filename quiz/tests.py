from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Choice
import time

class QuizTimerTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.question = Question.objects.create(text="Test Question")
        self.choice = Choice.objects.create(question=self.question, text="Choice 1", is_correct=True)
        self.quiz_url = reverse('quiz_view')
        self.submit_url = reverse('submit_quiz')

    def test_timer_starts_on_quiz_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.quiz_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('quiz_start_time', self.client.session)
        # Ensure start time is recent
        self.assertAlmostEqual(self.client.session['quiz_start_time'], time.time(), delta=5)

    def test_timer_clears_on_submit(self):
        self.client.login(username='testuser', password='testpassword')
        # First visit quiz to start timer
        self.client.get(self.quiz_url)
        self.assertIn('quiz_start_time', self.client.session)
        
        # Then submit
        response = self.client.post(self.submit_url, {str(self.question.id): str(self.choice.id)})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('quiz_start_time', self.client.session)
