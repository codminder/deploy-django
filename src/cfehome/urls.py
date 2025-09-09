from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world, name='hello-world'),
    path('health', views.health_view, name='health'),
    path('admin/', admin.site.urls),
]
