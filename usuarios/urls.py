from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.singout, name='logout'),
    path('address/', views.address, name='address'),
    path('addAddress/', views.addAddress, name='addAddress'),
]
