from django.db.models import Count

from .models import *


menu = [
        {'title': "Аптеки", 'url_name': 'pharmacies'},
        {'title': "Лекарственные средства", 'url_name': 'medicines'},
        {'title': "Заявки", 'url_name': 'application'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu

        return context
