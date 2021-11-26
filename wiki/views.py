from rest_framework import generics
from . import models
from . import serializers


class WikiPageCreateView(generics.CreateAPIView):
    serializer_class = serializers.WikiPageSerializer


class WikiPagesListView(generics.ListAPIView):
    serializer_class = serializers.WikiPageSerializer
    queryset = models.WikiPage.objects.all()


class WikiPageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WikiPageSerializer
    queryset = models.WikiPage.objects.all()


class PageVersionsListView(generics.ListAPIView):
    serializer_class = serializers.VersionPageSerializer
    queryset = models.PageVersion.objects.all()


class PageVersionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VersionPageSerializer
    queryset = models.PageVersion.objects.all()
