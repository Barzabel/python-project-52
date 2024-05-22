from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks_list'),
    path('<int:pk>/', views.TasksDetailView.as_view(), name='task_ditail'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),    
]

# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи