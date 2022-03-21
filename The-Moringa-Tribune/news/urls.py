
from django.urls import path
from .import views


# urlpatterns = [url('^$', views.welcome, name='welcome')]

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('today/', views.news_of_day, name='news-today')

]
