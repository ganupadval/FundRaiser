from django.conf import Settings, settings
from django.urls import path


from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('home/', views.home, name='home'),
    path('startup/', views.startup, name='startup'),
    path('medicalEm/', views.medicalEm, name='medicalEm'),
    path('contactUs/', views.contactUs, name='contactUS'),
    # path('signup/', views.signup, name='signup'),
]

