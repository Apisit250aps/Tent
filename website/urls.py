from django.urls import path

from . import views as page

urlpatterns = [
    path('', page.index_page, name='index'),
    
]