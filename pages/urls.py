from django.urls import path
from . import views

urlpatterns = [
    path('', views.myhttp),
    path('html/', views.aryan_html),
    path('cats/', views.cats, name="cats"),
    path('dogs/', views.dogs, name="dogs"),
    path('birds/', views.birds, name="birds"),
    path('rodents/', views.rodents, name="rodents"),
    path('reptiles/', views.reptiles, name="reptiles"),
]
