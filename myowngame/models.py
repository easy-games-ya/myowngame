from django.db import models

from django.contrib.auth.models import AbstractUser

from django.urls import reverse


class CustomUser(AbstractUser):
    '''Модель пользователя'''
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    # avatar = models.ImageField(upload_to='user_images', null=True, blank=True)
    avatar = models.ImageField(upload_to='user_images', blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, default='male', verbose_name='Пол')
    count = models.IntegerField(default=0, verbose_name='Общий счет')
    count_game = models.IntegerField(default=0, verbose_name='Счет в игре')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ContactModel(models.Model):
    '''Модел обратной связи'''
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=5000)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        db_table = 'ContactModel'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class CategoryModel(models.Model):
    '''Модель категории вопросов'''
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'CategoryModel'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class QuestionModel(models.Model):
    '''Модель вопросов'''
    answer = models.CharField(max_length=512, verbose_name='Ответ')
    question = models.CharField(max_length=512, verbose_name='Вопрос')
    score = models.IntegerField(verbose_name='Баллы')

    image = models.ImageField(upload_to='question_images', null=True, blank=True)

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'QuestionModel'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

