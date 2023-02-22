from django.urls import path
from django.contrib.auth import views as auth_views
from .views import article_create, article_edit, article_detail,signup, expert_signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('expert_signup/', expert_signup, name='expert_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', article_create, name='article_create'),
    path('<int:pk>/', article_detail, name='article_detail'),
    path('<int:pk>/edit/', article_edit, name='article_edit'),
]