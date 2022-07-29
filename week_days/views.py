from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

days_in_a_week = {
    'monday': 'Понедельник в Оптикарте день тяжелый, как в принципе и любой другой день',
    'tuesday': 'Вторник мало чем отличается от понедельника',
    'wednesday': 'Среда маленькая пятница',
    'thursday': 'Обычно проходит под девизом Тахир-гей!',
    'friday': 'Можно немного расслабиться',
    'saturday': 'Названа в честь Сатурна? Работа-Учеба',
    'sunday': 'Работа-Учеба'
}


def week_days(request, week_day):
    description = days_in_a_week.get(week_day)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Нет такого дня недели как {week_day}")


def week_days_by_number(request, week_day: int):
    list_week_days = list(days_in_a_week)
    if week_day < len(list_week_days):
        current_day = list_week_days[week_day-1]
        return HttpResponseRedirect(f"/todo_week/{current_day}")
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {week_day}")
