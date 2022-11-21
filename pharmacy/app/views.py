from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


menu = ['Аптеки', 'Лекарственные средства', 'Заявки', "О сайте"]


def index(request):
    return render(request, 'pharmacy/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'pharmacy/about.html', {'title': 'О сайте'})
