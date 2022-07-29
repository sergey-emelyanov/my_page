from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def signs_of_zodiack_by_str(request, sign_zodiack: str):
    description = zodiac_dict.get(sign_zodiack)
    if description:
        return HttpResponse(f"{description}")
    else:
        return HttpResponseNotFound(f"У нас нет такого знака как {sign_zodiack}")


def signs_of_zodiack_by_int(request, sign_zodiack: int):
    list_of_zodiacks = list(zodiac_dict)
    if sign_zodiack <= len(list_of_zodiacks):
        name_zodiack = list_of_zodiacks[sign_zodiack-1]
        return HttpResponseRedirect(f'/horoscope/{name_zodiack}')
    else:
        return HttpResponseNotFound(f"У нас нет такого знака как {sign_zodiack}")
