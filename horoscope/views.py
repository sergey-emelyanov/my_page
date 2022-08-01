from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {

	'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
	'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
	'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
	'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
	'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
	'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
	'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
	'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
	'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
	'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
	'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
	'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

types_dict = {
	'fire': ['aries', 'leo', 'sagittarius'],
	'earth': ['taurus', 'virgo', 'capricorn'],
	'air': ['gemini', 'libra', 'aquarius'],
	'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
	zodiacs = list(zodiac_dict)
	li_elements = ' '
	for sign in zodiacs:
		redirect_path = reverse('horoscope_names', args=[sign])
		li_elements += f"<li><a href={redirect_path}>{sign}</a></li>"
	response = f"<ul>{li_elements}</ul>"
	return HttpResponse(response)


def type(request):
	types_list = list(types_dict)
	li_elements = ' '
	for type in types_list:
		redirect_path = reverse('element_types',args=[type])
		li_elements += f"<li><a href={redirect_path}>{type.title()}</a></li>"
	response = f"<ul>{li_elements}</ul>"
	return HttpResponse(response)


def elements(request, element):
	types = types_dict.get(element)
	if types:
		li_elements = ' '
		for type in types:
			redirect_path = reverse('horoscope_names', args=[type])
			li_elements += f"<li><a href= {redirect_path}>{type.title()}</a></li>"
		response = f"<ul>{li_elements}</ul>"
		return HttpResponse(response)
	else:
		return HttpResponseNotFound("Нет такой стихии")



def signs_of_zodiack_by_str(request, sign_zodiack: str):
	description = zodiac_dict.get(sign_zodiack)
	if description:
		return HttpResponse(f"{description}")
	else:
		return HttpResponseNotFound(f"У нас нет такого знака как {sign_zodiack}")


def signs_of_zodiack_by_int(request, sign_zodiack: int):
	list_of_zodiacks = list(zodiac_dict)
	if sign_zodiack <= len(list_of_zodiacks):
		name_zodiack = list_of_zodiacks[sign_zodiack - 1]
		redirect_url = reverse('horoscope_names', args=[name_zodiack])
		return HttpResponseRedirect(redirect_url)
	else:
		return HttpResponseNotFound(f"У нас нет такого знака как {sign_zodiack}")
