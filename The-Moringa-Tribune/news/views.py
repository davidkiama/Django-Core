
from ast import Str
import datetime as dt
from django.http import HttpResponse, Http404


# Create your views here.


def welcome(request):
    return HttpResponse('Welcome to the Moringa tribune')


def news_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)

    html = f''' 
    <html>
        <body>
            <h1>News for {day} {date.day} - {date.month} - {date.year}  </h1>
        </body>
    </html>
    '''
    return HttpResponse(html)


def convert_dates(dates):
    # function that gets the weekday number
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day


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

    day = convert_dates(date)
    html = f''' 
    <html>
        <body>
            <h1>News for {day} {date.day} - {date.month} - {date.year}  </h1>
        </body>
    </html>
    '''

    return HttpResponse(html)
