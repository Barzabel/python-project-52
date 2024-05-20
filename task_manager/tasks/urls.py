from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks_list'),
#    path('<int:pk>', views.TasksView.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    # path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    # path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),    
]

# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи