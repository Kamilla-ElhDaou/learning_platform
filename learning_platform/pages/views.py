from django.shortcuts import render

app_name = 'pages'


def index(request):
    """Отображает главную страницу сайта."""
    return render(request, 'pages/index.html')


def about(request):
    """Отображает старницу с инфоормацией о компании."""
    return render(request, 'pages/about.html')


def contacts(request):
    """Отображает старницу с инфоормацией о компании."""
    return render(request, 'pages/contacts.html')


def profile(request):
    """Отображает старницу с инфоормацией о компании."""
    return render(request, 'pages/profile.html')
