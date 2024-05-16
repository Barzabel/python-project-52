from django.urls import path
from task_manager.status import views


urlpatterns = [
    path('', views.StatusView.as_view(), name='status_list'),
    path('create/', views.CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/', views.UpdateStatus.as_view(), name='update_status'),
    path('<int:pk>/delete/', views.DeleteStatus.as_view(), name='delete_status'),    
]
