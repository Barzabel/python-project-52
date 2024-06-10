from django.urls import path
from task_manager.status.views import (UpdateStatus,
                                       DeleteStatus,
                                       StatusView,
                                       CreateStatus)


urlpatterns = [
    path('', StatusView.as_view(), name='status_list'),
    path('create/', CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete_status'),
]
