
from xml.dom.minidom import Document
from django.urls import path, register_converter
from .import views
from .converters import DateConverter

register_converter(DateConverter, 'date')


# urlpatterns = [url('^$', views.welcome, name='welcome')]

urlpatterns = [

    path('', views.news_of_day, name='news-today'),
    path('archives/<date:past_date>/',
         views.past_days_news, name='pastNews'),
    path('search', views.search_results, name='search_results'),
    path('article/<id>', views.article, name='article')

]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
