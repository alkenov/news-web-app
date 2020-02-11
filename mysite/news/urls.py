from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
]