from django.forms import ModelForm, CharField

from apps.models import Task, Vacancy


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class VacancyForm(ModelForm):

    class Meta:
        model = Vacancy
        fields = '__all__'


