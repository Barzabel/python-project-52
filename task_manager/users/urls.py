from django.urls import path
from task_manager.users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.UseersView.as_view(), name='users'),
    path('create/', views.RegisterUser.as_view(), name='singup'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),    
]



"""
GET /users/ — страница со списком всех пользователей
GET /users/create/ — страница регистрации нового пользователя
POST /users/create/ — создание пользователя
GET /users/<int:pk>/update/ — страница редактирования пользователя
POST /users/<int:pk>/update/ — обновление пользователя
GET /users/<int:pk>/delete/ — страница удаления пользователя
POST /users/<int:pk>/delete/ — удаление пользователя

"""