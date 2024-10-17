from django.contrib import admin
from .models import Stock, StockData, Analysis

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'industry', 'created_at')
    search_fields = ('symbol', 'name')

@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'open_price', 'close_price', 'high', 'low', 'volume')
    list_filter = ('stock', 'date')
    search_fields = ('stock__symbol',)

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'moving_average', 'rsi', 'macd')
    list_filter = ('stock', 'date')
    search_fields = ('stock__symbol',)
