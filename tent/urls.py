from django.urls import path
from . import views as api


urlpatterns = [
    # auth
    path('auth-login', api.login, name='login-api'),
    path('auth-register', api.register, name='register-api'),
    
    
    
]