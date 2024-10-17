from django.urls import path
from . import views

app_name = 'stock_analysis'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('stocks/', views.stock_list_view, name='stock_list'),
    path('stocks/<str:symbol>/', views.stock_detail_view, name='stock_detail'),
    # Add other URL patterns as needed
]
