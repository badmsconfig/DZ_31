from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)
    # Основные типы полей
    # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты (blob)
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # связь с тегом
    tags = models.ManyToManyField(Tag)
    # Два варианта хронения картинок
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    def __str__(self):
        return self.name

class Imajes(models.Model):
    name = models.ImageField()
    description = models.TextField(blank=True)
    # связь с тегом
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Search(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Другие поля вашей модели

    def __str__(self):
        return self.title

