from django.conf.urls import url
from .views import CreateTaskView, TaskListView, task_create, task_list, task_update, task_delete

app_name = 'tasks'

urlpatterns = [
    url(r'^create-task/$', CreateTaskView.as_view(), name='create_task'),
    url(r'^create/$', task_create, name='task_create'),
    url(r'^$', task_list, name='task_list'),
    url(r'^(?P<pk>\d+)/update/$', task_update, name='task_update'),
    url(r'^(?P<pk>\d+)/delete/$', task_delete, name='task_delete'),
]
