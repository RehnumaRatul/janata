from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='visualization-index'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update)
]
