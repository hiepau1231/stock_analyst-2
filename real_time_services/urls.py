from django.urls import path
from . import views

app_name = 'real_time_services'

urlpatterns = [
    path('ws/', views.websocket_view, name='websocket'),
    # Add other URL patterns as needed
]
