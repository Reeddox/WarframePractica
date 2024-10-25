from django.contrib import admin
from django.urls import path

from WarframePracticaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('WarframeListado/', views.WarframeListado),
    path('AgregarWarframe/', views.AgregarWarframe),
    path('EliminarWarframe/<int:id>', views.EliminarWarframe),
    path('ModificarDatos/<int:id>', views.ModificarDatos)
]