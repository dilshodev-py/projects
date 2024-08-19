from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, DeleteView

from apps.forms import TaskForm, VacancyForm
from apps.models import Task, Vacancy, Company


class TaskListView(ListView):
    queryset = Task.objects.filter()
    context_object_name = 'tasks'
    template_name = 'apps/task-list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'apps/task-detail.html'


class TaskFormView(FormView):
    form_class = TaskForm
    success_url = 'task-list'
    template_name = 'apps/task-form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'apps/task-form.html', {'form': form})
        return redirect('task-list')


class TaskDeleteView(View):
    model = Task
    template_name = 'apps/task-list.html'
    success_url = reverse_lazy('task_list')

    def get(self, request, pk):
        Task.objects.filter(pk=pk).first().delete()
        return redirect('task-list')


class VacancyListView(ListView):

    queryset = Vacancy.objects.all()
    context_object_name = 'vacancies'
    template_name = 'apps/vacancy-list.html'



    def get_queryset(self):
        print(self.a)
        return super().get_queryset()


class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancy_list')


class VacancyFormView(FormView):
    form_class = VacancyForm
    template_name = 'apps/vacancy-form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vacancy_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['companies'] = Company.objects.all()
        data['types'] = Vacancy.Type.values
        return data
