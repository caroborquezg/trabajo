from django.urls import path

from AppCoder import views
from ProyectoCoder.AppCoder.views import mostrarfamiliar

urlpatterns = [

    path('',views.inicio),
    path('familia', views.mostrarfamiliar)
]
