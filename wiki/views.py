from rest_framework import generics
from . import models
from . import serializers


class WikiPageCreateView(generics.CreateAPIView):
    serializer_class = serializers.PageSerializer


class WikiPageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PageSerializer
    queryset = models.Page.objects.all()


class WikiPagesListView(generics.ListAPIView):
    serializer_class = serializers.PageListSerializer
    queryset = models.Page.objects.all()


class PageVersionListView(generics.ListAPIView):
    serializer_class = serializers.PageVersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('pk')
        history = models.Page.version.filter(id=page_id)
        return history

'''
class PageVersionCreate(generics.CreateAPIView):
    serializer_class = serializers.PageVersionSerializer


class PageVersionsListView(generics.ListAPIView):
    serializer_class = serializers.PageVersionSerializer
    queryset = models.PageVersion.objects.all()


class PageVersionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PageVersionSerializer
    queryset = models.PageVersion.objects.all()
'''