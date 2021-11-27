from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from . import models
from . import serializers


class PageCreateView(generics.CreateAPIView):
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )


class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )
    queryset = models.Page.objects.all()


class PagesListView(generics.ListAPIView):
    serializer_classes = serializers.PageSerializer
    queryset = models.Page.objects.all()


class VersionsListView(generics.ListAPIView):
    serializer_class = serializers.PageVersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('pk')
        history = models.Page.history.filter(id=page_id)
        return history


class VersionDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.PageVersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('page')
        history_id = self.kwargs.get('pk')
        history = models.Page.history.filter(
            id=page_id
        ).filter(
            history_id=history_id
        )
        return history
