from unicodedata import name
from django.urls import path
from django.contrib import admin
#from .views import SignUpView, PasswordChangeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('signup/', SignUpView.as_view(), name="signup"),
    #path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),

    # path('password_change_done/',
    #  PasswordChangeView.as_view(), name='password_change'),

    # path('password_reset_form/', PasswordChangeView.as_view(),
    #  name="password_reset_form",)
    # path('password_reset_form/', PasswordChangeView.as_view(),
    # name='password_reset_form'),

]
