from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('events', views.events, name='events'),
    # path('staff', views.staff, name='staff'),
    # path('about', views.about, name='about'),
]