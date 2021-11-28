from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from . import models
from . import serializers


class PageCreateView(generics.CreateAPIView):
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )


class PageListView(generics.ListAPIView):
    serializer_class = serializers.PageSerializer
    queryset = models.Page.objects.all()


class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )
    queryset = models.Page.objects.all()


class VersionListView(generics.ListAPIView):
    serializer_class = serializers.VersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('pk')
        versions = models.Page.history.filter(id=page_id)
        return versions


class VersionDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.VersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('page')
        version_id = self.kwargs.get('pk')
        version = models.Page.history.filter(
            id=page_id
        ).filter(
            history_id=version_id
        )
        return version


class SetCurrentVersionView(generics.RetrieveAPIView):
    serializer_class = serializers.VersionSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        version_id = self.kwargs.get('pk')
        history_instance = models.Page.history.get(history_id=version_id)
        history_instance.instance.save_without_historical_record()
        current_version = models.Page.history.filter(
            history_id=version_id
        )
        return current_version
