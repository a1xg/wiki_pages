from django.db import models


class WikiPage(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class PageVersion(models.Model):
    wiki_page = models.ForeignKey('WikiPage', on_delete=models.CASCADE, blank=False, related_name="versions")
    title = models.CharField(blank=False, max_length=300)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
