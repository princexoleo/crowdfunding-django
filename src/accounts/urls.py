from django.contrib import admin
from django.urls import path,include
from accounts import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home_view, name='home' ),
    path('home/', views.home_view, name='home' ),
    path('login/', views.login_view, name='login' ),
    path('register/', views.signup, name='register' ),
    path('logout/', views.logout_view, name='logout' ),
    path('startup/', views.startup_view, name='startup' ),
    path('hospital/', views.hospital_view, name='hospital' ),
    path('education/', views.education_view, name='education' ),
    path('contact/', views.contact_view, name='contact' ),
    path('dashboard/', views.dashboard_view, name='dashboard' ),
    
]
