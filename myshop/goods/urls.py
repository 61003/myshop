from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoodsList.as_view(), name='goods'),
]
