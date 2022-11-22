from django.urls import path

from app.views import *

urlpatterns = [
    path('', PharmacyView.as_view(), name='home'),
    path('pharmacies/', PharmacyView.as_view(), name='pharmacies'),
    path('medicines/', MedicinesView.as_view(), name='medicines'),
    path('application/', ApplicationView.as_view(), name='application'),
    path('application/add_application/', AddApplication.as_view(), name='add_application'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]