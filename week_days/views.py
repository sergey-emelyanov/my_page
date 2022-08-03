from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
		current_day = list_week_days[week_day - 1]
		redirect_url = reverse('week_days', args=[current_day])
		return HttpResponseRedirect(redirect_url)
	else:
		return HttpResponseNotFound(f"Неверный номер дня - {week_day}")


def index(request):
	return render(request, 'week_days/greeting.html')

def beautiful_table(request):
	return render(request, 'week_days/beautiful_table.html')
