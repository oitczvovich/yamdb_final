from django.contrib.auth.models import AbstractUser
from django.core.validators import (EmailValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)
from django.db import models

from .validators import validate_title_year


class User(AbstractUser):
    """Модель юзер."""

    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER_ROLE = [
        ('user', USER),
        ('admin', ADMIN),
        ('moderator', MODERATOR),
    ]

    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-_]+$',
                message='Недопустимое имя',
            )
        ],
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
        validators=[EmailValidator],
    )
    first_name = models.TextField('Имя', max_length=150, blank=True)
    last_name = models.TextField('Фамилия', max_length=150, blank=True)
    bio = models.TextField('Дополнительная информация', blank=True)
    role = models.CharField(
        'Роль', max_length=30, choices=USER_ROLE, default='user'
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique_username_email',
            ),
        ]


class Genre(models.Model):
    """Модель жанра."""

    name = models.CharField('Жанр', max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категории."""

    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения."""

    name = models.CharField('Произведение', max_length=500)
    year = models.SmallIntegerField(
        'Год выпуска', db_index=True, validators=(validate_title_year,)
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre, through='GenreTitle', verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='Категория',
    )
    rating = models.IntegerField('Рейтинг', default=None, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Вспомогательная модель жанров произведения."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
    )

    class Meta:
        verbose_name_plural = 'Произведения и жанры'

    def __str__(self):
        return f'{self.title}, {self.genre}'


class Review(models.Model):
    """Модель отзывов."""

    title = models.ForeignKey(
        Title,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Произведение',
    )
    text = models.TextField(verbose_name='Отзыв')
    author = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, 'Поставьте рейтинг от 1 до 10'),
            MaxValueValidator(10, 'Поставьте рейтинг от 1 до 10'),
        ],
        verbose_name='Рейтинг',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'), name='distinct_review'
            ),
        ]

    def __str__(self):
        return self.text[:42]


class Comment(models.Model):
    """Модель комментариев."""

    review = models.ForeignKey(
        Review,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
    )
    text = models.TextField(
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:42]
