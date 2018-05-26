# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json
from .forms import CreateTaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

@login_required()
def task_list(request):
    template_name = 'tasks/tasklist.html'
    query = request.GET.get('q')
    if query:
        query = query.strip()
        object_list = Task.objects.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
        )
    else:
        object_list = Task.objects.all()
    return render(request, template_name, {'object_list': object_list})

@login_required()
def save_task_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            object_list = Task.objects.all()
            data['html_task_list'] = render_to_string('tasks/partial_task_list.html', {
                'object_list': object_list
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required()
def task_create(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
    else:
        form = CreateTaskForm(initial={'owner' :  request.user,
                                    'assignee' :  request.user})
    return save_task_form(request, form, 'tasks/partial_task_create.html')

@login_required()
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
    else:
        form = CreateTaskForm(instance=task)
    return save_task_form(request, form, 'tasks/partial_task_update.html')

@login_required()
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    data = dict()
    if request.method == 'POST':
        task.delete()
        data['form_is_valid'] = True
        object_list = Task.objects.all()
        data['html_task_list'] = render_to_string('tasks/partial_task_list.html', {
            'object_list': object_list
        })
    else:
        context = {'task': task}
        data['html_form'] = render_to_string('tasks/partial_task_delete.html', context, request=request)
    return JsonResponse(data)


class HomeView(TemplateView):
    template_name = "base.html"


class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    #template_name = 'tasks/createtask.html'
    #success_url = reverse_lazy('tasks:list_task')

    def get_form_kwargs(self):
        kwargs = super(CreateTaskView, self).get_form_kwargs()
        kwargs.update({'initial': {'owner' : self.request.user,
                                   'assignee' : self.request.user}})
        return kwargs

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.assignee = self.request.user
        return super(CreateTaskView, self).form_valid(form)

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasklist.html'
    model = Task
