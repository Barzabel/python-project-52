from django.urls import path
from homepage import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('users/', views.UseersView.as_view(), name='users'),
    path('users/create/', views.RegisterUser.as_view(), name='singup'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]



"""
GET /users/ — страница со списком всех пользователей
GET /users/create/ — страница регистрации нового пользователя
POST /users/create/ — создание пользователя
GET /users/<int:pk>/update/ — страница редактирования пользователя
POST /users/<int:pk>/update/ — обновление пользователя
GET /users/<int:pk>/delete/ — страница удаления пользователя
POST /users/<int:pk>/delete/ — удаление пользователя
GET /login/ — страница входа +
POST /login/ — аутентификация (вход) +
POST /logout/ — завершение сессии (выход) ?
"""