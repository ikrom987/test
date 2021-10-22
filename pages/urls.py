
from django.contrib.auth import logout
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('detail/<int:p_id>/', views.detail, name='detail'),
    path('category/<int:c_id>/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('login/', views.login, name="login"),
    path('tekshirish/', views.tekshirish, name='tekshirish'),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.reg, name="reg"),
    path('signup/create/', views.reg_create, name="reg_create"),
]
