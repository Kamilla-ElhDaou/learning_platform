from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .models import Course, Lesson, Progress, Profile, Test


class CourseListView(ListView):
    """Отображает страницу с опубликованными курсами."""

    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = Course.objects.filter(is_published=True)
        return queryset


class CourseDetailView(DetailView):
    """Отображает страницу курса."""

    model = Course
    template_name = 'courses/course_detail.html'
    slug_url_kwarg = 'course_slug'
    context_object_name = 'course'

    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=True
        ).prefetch_related('lessons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lessons.filter(
            is_published=True
        ).order_by('order')
        return context


class LessonDetailView(DetailView):
    """Отображает страницу с определнным уроком."""

    model = Lesson
    template_name = 'courses/lesson_detail.html'
    slug_url_kwarg = 'lesson_slug'
    context_object_name = 'lesson'

    def get_queryset(self):
        return Lesson.objects.filter(
            course__slug=self.kwargs['course_slug'],
            is_published=True
        )
