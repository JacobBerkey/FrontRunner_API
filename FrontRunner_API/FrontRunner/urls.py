from django.urls import path
from . import views

urlpatterns = [
    path('FrontRunner/', views.PersonList.as_view()),
]
