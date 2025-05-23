from django.urls import path

from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path(
        '<slug:course_slug>/',
        views.CourseDetailView.as_view(),
        name='course_detail',
    ),
    path(
        '<slug:course_slug>/<slug:lesson_slug>/',
        views.LessonDetailView.as_view(),
        name='lesson_detail',
    ),
]