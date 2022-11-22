from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from app.forms import *
from app.utils import *

# Create your views here.


class PharmacyView(DataMixin, ListView):
    model = Pharmacy
    template_name = 'pharmacy/index.html'
    context_object_name = 'pharmacy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Pharmacy.objects.filter(name=query)

        return Pharmacy.objects.all()


class MedicinesView(DataMixin, ListView):
    model = MedicamentInPharmacy
    template_name = 'pharmacy/medicines.html'
    context_object_name = 'medicines'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Лекарственное средство")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        query = self.request.GET.get('q')

        return MedicamentInPharmacy.objects.filter(medicament__name=query)


class ApplicationView(DataMixin, ListView):
    model = Application
    template_name = 'pharmacy/application.html'
    context_object_name = 'application'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Заявки")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        user = self.request.user
        return Application.objects.prefetch_related('medicines').filter(user=user)


class AddApplication(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddApplicationForm
    template_name = 'pharmacy/addapplication.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление заявки")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):

        obj = Application()
        obj.user = self.request.user
        obj.reason = form.cleaned_data["reason"]

        obj.total_price = 0.0
        obj.save()
        for u in form.cleaned_data["medicines"]:
            print(type(u.id))
            obj.medicines.add(u.id)
        # user = form.save()
        # login(self.request, user)
        return redirect('home')


def about(request):
    return render(request, 'pharmacy/about.html', {'title': 'О сайте', 'menu': menu})


def login(request):
    return HttpResponse("Авторизация")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'pharmacy/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'pharmacy/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
