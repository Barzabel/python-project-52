from django.urls import path
from task_manager.tasks.views import (TasksView,
                                      TasksDetailView,
                                      CreateTask,
                                      UpdateTask,
                                      DeleteTask)


urlpatterns = [
    path('', TasksView.as_view(), name='tasks_list'),
    path('<int:pk>/', TasksDetailView.as_view(), name='task_ditail'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
]
