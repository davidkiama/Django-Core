
from django.shortcuts import redirect, render
import datetime as dt
from django.http import HttpResponse, Http404

from .models import Article


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    return render(request, 'all-news/today-news.html', {'date': date, 'news': news})


def past_days_news(request, past_date):

    # check if the passed in object is truly a date
    if past_date.year:
        date = past_date
    else:
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)

    return render(request, 'all-news/past-news.html', {'date': date, 'news': news})
