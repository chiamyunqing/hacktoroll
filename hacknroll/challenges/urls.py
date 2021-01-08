from django.urls import path, reverse_lazy
from . import views

app_name='challenges'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
