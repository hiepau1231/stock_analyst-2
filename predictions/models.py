from django.db import models
from apps.stock_analysis.models import Stock

class Prediction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='predictions')
    prediction_date = models.DateField()
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stock', 'prediction_date')
        ordering = ['-prediction_date']

    def __str__(self):
        return f"Prediction for {self.stock.symbol} on {self.prediction_date}"
