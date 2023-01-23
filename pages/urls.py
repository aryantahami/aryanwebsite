from django.urls import path
from . import views

urlpatterns = [
    path('', views.myhttp),
    path('html', views.aryan_html),
    path('metaverse', views.meta),
]
