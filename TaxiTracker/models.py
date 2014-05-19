from django.db import models 
from django.db.models.query import QuerySet

class taximap(models.Model):

    companyname = models.CharField(max_length=100)
    nelat = models.DecimalField(max_digits=20, decimal_places=15) 
    nelng = models.DecimalField(max_digits=20, decimal_places=15)
    swlat = models.DecimalField(max_digits=20, decimal_places=15)
    swlng = models.DecimalField(max_digits=20, decimal_places=15)

