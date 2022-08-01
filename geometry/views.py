from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


def get_rectangle_area(request, length: int, width: int):
	return HttpResponse(f"Площадь прямоугольника с шириной  {length} и длиной {width} составляет {length * width} ")


def get_square_area(request, length: int):
	return HttpResponse(f"Площадь квадрата со сторной {length} состаляет {length ** 2}")


def get_circle_area(request, radius):
	return HttpResponse(f"Площадь круга с радиусом {radius} составляет {pi * (radius ** 2):.2f} ")


def rectangle_area(request, length: int, width: int):
	redirect_url = reverse('rectangle', args=[length, width])
	return HttpResponseRedirect(redirect_url)


def square_area(request, length: int):
	redirect_url = reverse('square', args=[length])
	return HttpResponseRedirect(redirect_url)


def circle_area(request, radius:int):
	redirect_url = reverse('circle', args=[radius])
	return HttpResponseRedirect(redirect_url)
