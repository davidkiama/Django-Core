
from django.shortcuts import redirect, render
import datetime as dt
from django.http import HttpResponse, Http404


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def news_of_day(request):
    date = dt.date.today()

    return render(request, 'all-news/today-news.html', {'date': date})


# def convert_dates(dates):
#     # function that gets the weekday number
#     day_number = dt.date.weekday(dates)

#     days = ['Monday', 'Tuesday', 'Wednesday',
#             'Thursday', 'Friday', 'Saturday', 'Sunday']

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day


def past_days_news(request, past_date):
    # try:
    #     # converts date from the string
    #     date = dt.datetime.strftime(past_date, '%Y-%m-%d').date()
    #     print('************************')
    #     print(date)
    # except:
    #     # Raise error when valueError is thrown
    #     raise Http404()

    # check if the passed in object is truly a date
    if past_date.year:
        date = past_date
    else:
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {'date': date})
