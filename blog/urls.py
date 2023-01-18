from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_page, name='listing_page'),
    path('<int:pk>/', views.detail_page, name='detail_page'),
]

# path('<int:pk>/', views.detail_page, name='detail_page'),
# path('detail_page/', views.detail_page, name='detail_page'),
