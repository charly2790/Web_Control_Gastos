"""Web_Control_Gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Web_Control_Gastos.views import alta_tipo_operacion,mostrar_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alta_tipo_operacion/',alta_tipo_operacion,name='alta_tipo_operacion'),
    path('mostrar_datos/<tipo_operacion_name>,<tipo_operacion_descripcion>',mostrar_datos),
]
