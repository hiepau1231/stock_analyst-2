from django.urls import path
from . import views

app_name = 'predictions'

urlpatterns = [
    path('list/', views.prediction_list_view, name='prediction_list'),
    path('<int:pk>/', views.prediction_detail_view, name='prediction_detail'),
    # Add other URL patterns as needed
]
