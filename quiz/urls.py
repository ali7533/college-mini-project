from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.quiz_view, name='quiz_view'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
]
