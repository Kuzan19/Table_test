from django.shortcuts import render
from django.views.generic import ListView

from .models import UserModel


class TableView(ListView):
    """Класс отображения данных из таблицы UserModel"""
    model = UserModel
    template_name = 'newapp/index.html'
    context_object_name = 'users'
    paginate_by = 20

    def get_ordering(self):
        """Функция сортировки по переданному атрибуту 'orderby' """
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_queryset(self):
        """Функция фильтрации под переданному атрибуту 'filter_by', если он передается"""
        if self.request.GET.get('filter_by'):
            filtering = self.request.GET.get('filter_by')
            queryset = UserModel.objects.filter(gender=filtering)
        else:
            queryset = UserModel.objects.all()
        return queryset


# def new_data_base(request):
#     """Функция для генерирования случайных записей в таблице"""
#     try:
#         from mimesis.providers import Person
#
#         person = Person('ru')
#         for i in range(1000):
#             a = UserModel(name=person.name(),
#                           surname=person.surname(),
#                           age=person.age(),
#                           gender=person.gender(),
#                           phone_number=person.telephone(),
#                           blood_type=person.blood_type(),
#                           )
#             a.save()
#         return HttpResponse('База данных успешно загружена!')
#     except Exception:
#         print("Что-то пошло не так! :(")
