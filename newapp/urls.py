from django.urls import path
from . import views

urlpatterns = [
    path('', views.TableView.as_view(), name='table-views-page'),
    path('sort_by_name', views.SortedTableView.as_view(), name='sorted-name-table-views-page'),
    path('sort_by_age', views.SortedTableView.as_view(), name='sorted-age-table-views-page'),
    # path('create_new_strings_database', views.new_data_base),
]
