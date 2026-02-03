from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.category_list, name='category_list'),
    path('quiz/<int:category_id>/', views.quiz_view, name='quiz_view'),
    path('quiz/', views.quiz_view, name='quiz_view_all'), # Optional fallback
    path('submit/', views.submit_quiz, name='submit_quiz'),
]
