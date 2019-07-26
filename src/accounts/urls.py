from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home_view, name='home' ),
    path('login/', views.login_view, name='login' ),
    path('register/', views.register_view, name='register' ),
]
