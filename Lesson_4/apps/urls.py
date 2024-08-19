from django.urls import path
from apps.views import TaskListView, TaskDetailView, TaskFormView, TaskDeleteView, VacancyListView, VacancyDeleteView, \
    VacancyFormView

urlpatterns = [
    path('task/list' , TaskListView.as_view(), name='task_list'),
    path('task/detail/<int:pk>' , TaskDetailView.as_view(), name='task-detail'),
    path('task/form' , TaskFormView.as_view(), name='task-form'),
    path('task/list/<int:pk>' , TaskDeleteView.as_view(), name='task-delete'),
]



urlpatterns += [
    path('vacancy/list', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/delete/<int:pk>', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('vacancy/form', VacancyFormView.as_view(), name='vacancy_form'),


]
