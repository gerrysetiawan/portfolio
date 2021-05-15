from django.urls import path
from core_portfolio import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]