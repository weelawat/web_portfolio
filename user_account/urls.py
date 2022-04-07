from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="user_account/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]
