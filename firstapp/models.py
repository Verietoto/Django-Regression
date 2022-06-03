from django.db import models

# Create your models here.
class regression_db(models.Model):
    x_val = models.DecimalField(max_digits=6, decimal_places=3)
    y_val = models.DecimalField(max_digits=6, decimal_places=3)