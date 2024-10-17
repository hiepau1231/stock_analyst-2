from django.contrib import admin
from .models import Stock, StockData, Analysis

admin.site.register(Stock)
admin.site.register(StockData)
admin.site.register(Analysis)
