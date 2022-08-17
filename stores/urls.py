from django.urls import path
from . import views



urlpatterns = [
    path('', views.PizzeriaListAPIView.as_view(), name = 'pizzeria_list'),
    path('<int:id>/', views.PizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail'),
    path('create/', views.PizzeriaCreateAPIViews.as_view(), name='pizzeria_create')
]