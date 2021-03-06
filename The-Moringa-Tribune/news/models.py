
from email.policy import default
from django.db import models

# Create your models here.


class Editor(models.Model, ):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()


class Tags(models.Model, ):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


import datetime as dt


class Article(models.Model, ):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_field = models.DateTimeField(auto_now=True)
    article_image = models.ImageField(
        upload_to='articles/', default='default.img')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_field__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_field__date=date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
