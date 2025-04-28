from django.urls import path

from . import views


app_name = 'profile'

urlpatterns = [
    path(
        '<str:username>/',
        views.ProfileDetail.as_view(),
        name='profile',
    ),
    path(
        'profile/edit/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile',
    ),
    path(
        'profile/delete/',
        views.ProfileDeleteView.as_view(),
        name='delete_profile',
    ),
]