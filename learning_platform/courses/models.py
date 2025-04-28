from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


from .constants import LANGUAGE_CHOICES, LEVEL_CHOICES


class Profile(models.Model):
    """
    Модель для профиля пользователя.

    Атрибуты:
        user (OneToOneField): Пользователь.
        language (CharField): Изучаемый язык.
        language_level (CharField): Уровень языка пользователя.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
        default='english',
        verbose_name='Изучаемый язык',
    )
    language_level = models.CharField(
        max_length=50,
        choices=LEVEL_CHOICES,
        default='beginner',
        verbose_name='Уровень языка',
    )

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class Course(models.Model):
    """
    Модель для курса иностранного языка.

    Атрибуты:
        title (CharField): Название курса.
        slug (SlugField): Уникальный идентификатор для URL.
        description (TextField): Описание курса.
        language (CharField): Язык изучаемый на курсе.
        created_at (DateTimeField): Дата создания курса.
        is_published (BooleanField): Опубликовано.
    """

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name='URL',
    )
    description = models.TextField(verbose_name='Описание')
    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
        default='english',
        verbose_name='Язык курса',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[self.slug])


class Lesson(models.Model):
    """
    Модель для урока в курсе.

    Атрибуты:
        course (ForeignKey): Название курса.
        title (CharField): Название урока.
        slug (SlugField): Уникальный идентификатор для URL.
        content (TextField): Материал урока.
        example (TextField): Примеры в уроке.
        duration (PositiveIntegerField): Продолжительность урока.
        order (PositiveIntegerField): Позиция в курсе.
        language_level (CharField): Уровень языка к которому относится урок.
        is_published (BooleanField): Опубликовано.
    """

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        unique=True,
    )
    slug = models.SlugField(
        blank=True,
        verbose_name='URL',
    )
    content = models.TextField(verbose_name='Материал урока',)
    example = models.TextField(
        blank=True,
        null=True,
        verbose_name='Примеры',
    )
    duration = models.PositiveIntegerField(
        verbose_name='Длительность урока (в минутах)',
        default=30,
    )
    order = models.PositiveIntegerField(
        verbose_name='Позиция в курсе',
        default=0,
    )
    language_level = models.CharField(
        max_length=50,
        choices=LEVEL_CHOICES,
        default='beginner',
        verbose_name='Уровень языка',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('course', 'slug')
        ordering = ['course', 'order']
        verbose_name = 'урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson_detail', args=[
            self.course.slug,
            self.slug,
        ])


class Test(models.Model):
    """
    Модель для урока в курсе.

    Атрибуты:
        lesson (ForeignKey): Название урока.
        question (TextField): Название урока.
        option1 (CharField): Вариант ответа.
        option2 (CharField): Вариант ответа.
        option3 (CharField): Вариант ответа.
        option4 (CharField): Вариант ответа.
        passing_score (PositiveIntegerField): Проходной балл.
    """

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='tests',
        verbose_name='Урок',
    )
    question = models.TextField(verbose_name='Вопрос',)
    option1 = models.CharField(
        max_length=200,
        verbose_name='Вариант ответа 1',
        blank=True,
        default=None,
        null=True,
    )
    option2 = models.CharField(
        max_length=200,
        verbose_name='Вариант ответа 2',
        blank=True,
        default=None,
        null=True,
    )
    option3 = models.CharField(
        max_length=200,
        verbose_name='Вариант ответа 3',
        blank=True,
        default=None,
        null=True,
    )
    option4 = models.CharField(
        max_length=200,
        verbose_name='Вариант ответа 4',
        blank=True,
        default=None,
        null=True,
    )
    correct_answer = models.CharField(
        max_length=200,
        verbose_name='Правильный ответ',
    )
    passing_score = models.PositiveIntegerField(
        verbose_name='Проходной балл',
        default=70,
    )

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.question


class Progress(models.Model):
    """
    Модель для урока в курсе.

    Атрибуты:
        user (ForeignKey): Пользователь.
        lesson (ForeignKey): Текущий урок.
        completed (BooleanField): Статус выполнения.
        completed_at (DateTimeField): Дата завершения.
        score (PositiveIntegerField): Количество набранных очков.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='progress',
        verbose_name='Пользователь',
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Текущий урок',
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Статус выполнения',
    )
    completed_at = models.DateTimeField(
        verbose_name='Дата завершения',
        blank=True,
        null=True,
    )
    score = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество набранных очков',
    )

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name = 'прогресс'
        verbose_name_plural = 'Прогрессы'

    def __str__(self):
        return f'{self.user.username}, вы на {self.lesson.title} уроке'
