from django.db import models
from simple_history.models import HistoricalRecords


class Page(models.Model):
    title = models.CharField(blank=False, max_length=300)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(cascade_delete_history=True)

    def __str__(self):
        return str(self.title)

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret
