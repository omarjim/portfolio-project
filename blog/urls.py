from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:bloga_id>/', views.detail, name='detail')
]
