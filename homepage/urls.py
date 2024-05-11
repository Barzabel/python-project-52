from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),

]



"""
/users/
/login/
/users/create/
"""