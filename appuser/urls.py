from django.urls import path
from django.contrib.auth.views import  LoginView, LogoutView
from . import views
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', next_page='homepage'), name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('signup/', views.UserSignUpView.as_view(), name='signup')
]
