from django.contrib import admin
from django.urls import path
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipes/<str:name>/', views.recipe_detail, name='details'),
    path('add/', views.add_recipe, name='add'),
    path('edit/<str:name>/', views.edit_recipe, name='edit'),
    path('delete/<str:name>/', views.delete_recipe),
]
