from django.contrib import admin
from django.urls import path, include
from .views import LoginUser, IndexView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    #path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

#POST /logout/ — завершение сессии (выход) ?