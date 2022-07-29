from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


def get_rectangle_area(request, length: int, width: int):
    return HttpResponse(f"Площадь прямоугольника с шириной  {length} и длиной {width} составляет {length * width} ")


def get_square_area(request, length: int):
    return HttpResponse(f"Площадь квадрата со сторной {length} состаляет {length ** 2}")


def get_circle_area(request, radius):
    return HttpResponse(f"Площадь круга с радиусом {radius} составляет {pi * (radius ** 2):.2f} ")


def rectangle_area(request, length: int, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{length}/{width}')


def square_area(request, length: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{length}')


def circle_area(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
