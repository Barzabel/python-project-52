from django.urls import path
from task_manager.labels import views


urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels_list'),
    path('create/', views.CreateLabel.as_view(), name='create_label'),
    path('<int:pk>/update/', views.UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.DeleteLabel.as_view(), name='delete_label'),    
]

# GET /labels/ — страница со списком всех меток
# GET /labels/create/ — страница создания метки
# POST /labels/create/ — создание новой метки
# GET /labels/<int:pk>/update/ — страница редактирования метки
# POST /labels/<int:pk>/update/ — обновление метки
# GET /labels/<int:pk>/delete/ — страница удаления метки
# POST /labels/<int:pk>/delete/ — удаление метки