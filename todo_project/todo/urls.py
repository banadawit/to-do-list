from django.urls import path
from . import views
from django.urls import path
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
