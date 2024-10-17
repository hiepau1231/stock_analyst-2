from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('stock', 'prediction_date', 'predicted_price', 'confidence', 'created_at')
    list_filter = ('stock', 'prediction_date')
    search_fields = ('stock__symbol',)
