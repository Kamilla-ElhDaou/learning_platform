from django.contrib import admin

from .models import Course, Lesson, Progress, Profile, Test


admin.site.empty_value_display = 'Не задано'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'language',
        'created_at',
        'is_published',
    )
    search_fields = (
        'title',
        'language',
        )
    list_filter = (
        'language',
        'is_published',
    )
    list_display_links = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'title',
        'content',
        'example',
        'order',
        'language_level',
        'slug'
    )
    search_fields = (
        'course',
        'title',
        )
    list_filter = (
        'course',
    )
    list_display_links = ('title',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'language',
        'language_level',
    )
    search_fields = (
        'user',
        'language',
        )
    list_filter = (
        'language',
        'language_level',
    )
    list_display_links = ('user',)

@admin.register(Test)
class TestADmin(admin.ModelAdmin):
    list_display = (
        'lesson',
        'question',
        'correct_answer',
    )
    search_fields = (
        'lesson',
        'question',
        )
    list_filter = (
        'lesson',
    )
    list_display_links = ('lesson',)


admin.site.register(Progress)
