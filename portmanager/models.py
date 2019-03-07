from django.db import models

class PortAllocation(models.Model):
    port_number = models.IntegerField(primary_key=True)
    student = models.CharField(max_length=8)