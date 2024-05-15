from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    # path('create/', views.RegisterUser.as_view(), name='singup'),
    # path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    # path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),    
]
