from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


def monday(request):
    return HttpResponse("Понедельник в Оптикарте день тяжелый, как в принципе и любой другой день")


def tuesday(request):
    return HttpResponse("Вторник мало чем отличается от понедельника")


def week_days(request,week_day):
    if week_day == 'monday':
        return HttpResponse("Понедельник в Оптикарте день тяжелый, как в принципе и любой другой день")
    elif week_day == 'tuesday':
        return HttpResponse("Вторник мало чем отличается от понедельника")
    elif week_day == 'thursday':
        return HttpResponse("Среда маленькая пятница")
    else:
        return HttpResponseNotFound(f"Нет такого дня недели как {week_day}")

