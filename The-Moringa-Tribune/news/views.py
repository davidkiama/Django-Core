
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


def search_results(request):
    if 'article' in request.GET and request.GET['article']:

        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'all-news/search.html', {'message': message, 'articles': searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {'message': message})


def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404()
    return render(request, 'all-news/article.html', {'article': article})
