from django.urls import path
from . import views
urlpatterns = [
    path("", views.control, name="control" ),
    path("add/", views.control_add, name="control_add"),
    path('create/', views.control_create, name="control_create"),
    path("detail/<int:id>", views.control_detail, name="control_detail"),
    path('delete/', views.control_delete, name="control_delete")
]
