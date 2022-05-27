from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoodsList.as_view()),
    path('category/<int:id>/', views.CategoryGoodsList.as_view()),
]
