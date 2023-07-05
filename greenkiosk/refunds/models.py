from django.db import models

# Create your models here.
class Refunds(models.Model):
    orderId = models.IntegerField()
    refundsId = models.IntegerField()
    amount = models.DecimalField(max_digits= 15, decimal_places=2)
    reason = models.TextField(blank=False)
    requestDate = models.DateTimeField(auto_now_add=True)
    processedDate = models.DateTimeField()
    
