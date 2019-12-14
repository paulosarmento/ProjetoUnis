from django.urls import path
from . import views

app_name = "poolform"
urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.form_Save, name='calc')
]