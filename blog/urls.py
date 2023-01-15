
from django.urls import path
from . import views

urlpatterns = [
    path('listing_page/', views.listing_page, name='listing-page'),
    path('detail_page/', views.detail_page, name='detail-page'),
]
