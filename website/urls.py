from django.urls import path

from . import views as page

urlpatterns = [
    path('', page.index_page, name='index'),
    
    path('auth-login', page.login_page, name='login-page'),
    path('auth-register', page.register_page, name='register-page'),
    
    
    
]