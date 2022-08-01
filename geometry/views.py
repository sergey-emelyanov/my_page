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


def rectangle_area(request):
	return render(request, 'geometry/rectangle.html')


def square_area(request):
	return render(request, 'geometry/square.html')


def circle_area(request):
	return render(request, 'geometry/circle.html')
