from django.urls import path
from .import views
urlpatterns = [
    path('signup/', views.register),
    path('login/', views.login0),
    path('home/',views.show),

]
