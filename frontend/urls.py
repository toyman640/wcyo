from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('about-us', views.about, name='about'),
]