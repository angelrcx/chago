# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),  # Página de inicio
    path('login/', views.login_view, name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logut/',views.logout_view,name = "logout"),
]
