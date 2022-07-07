from django.conf import Settings, settings
from django.urls import path


from . import views

urlpatterns = [
        path('handlerequest/', views.handlerequest, name='handlerequest'),
    
]
