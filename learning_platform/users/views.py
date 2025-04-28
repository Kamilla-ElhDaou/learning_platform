from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy


User = get_user_model()


class UserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('profile:profile')


class ProfileDetail(DetailView):
    ...


class ProfileUpdateView(UpdateView):
    ...


class ProfileDeleteView(DeleteView):
    ...
