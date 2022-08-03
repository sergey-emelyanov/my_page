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

def people(request):
	people = [
		{'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
		{'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
		{'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
		{'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
		{'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
		{'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
		{'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
		{'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
		{'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
		{'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
	]
	data = {
		'people': people
	}
	return render(request, 'geometry/people.html', context=data)
