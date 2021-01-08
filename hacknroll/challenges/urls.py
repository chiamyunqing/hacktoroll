from django.urls import path, reverse_lazy
from . import views

app_name='challenges'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('chal2/', views.challenge2.as_view(), name='c2'),
    path('c3/', views.challenge3.as_view(), name='c3'),
    path('cv', views.cookieview, name='cookie_view'),
]
