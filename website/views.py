from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_page(request):
    
    return render(request, 'auth/login.html')

def register_page(request):
    
    return render(request, 'auth/register.html')





@login_required()
def index_page(request):
    
    return render(request, 'admin/index.html')