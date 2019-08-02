from django.urls import path,include
from donations import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.donation_view, name='donation' ),
]
