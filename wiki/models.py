from django.db import models
from simple_history.models import HistoricalRecords


class Page(models.Model):
    title = models.CharField(blank=False, max_length=300)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    version = HistoricalRecords()