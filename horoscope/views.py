from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def aries(request):
	return HttpResponse("Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")


def taurus(request):
	return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")


def signs_of_zodiack(request,sign_zodiack):
	if sign_zodiack == "aries":
		return HttpResponse("Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")
	elif sign_zodiack == "taurus":
		return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
	elif sign_zodiack == "gemini":
		return HttpResponse("Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
	else:
		return HttpResponseNotFound(f"У нас нет такого знака как {sign_zodiack}")


