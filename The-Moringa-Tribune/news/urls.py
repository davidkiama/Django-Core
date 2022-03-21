
from django.urls import path, register_converter
from .import views
from .converters import DateConverter

register_converter(DateConverter, 'date')


# urlpatterns = [url('^$', views.welcome, name='welcome')]

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('today/', views.news_of_day, name='news-today'),
    path('archives/<date:past_date>/',
         views.past_days_news, name='pastNews')

]
