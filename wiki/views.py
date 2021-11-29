from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from . import models
from . import serializers


class PageCreateView(generics.CreateAPIView):
    """
    To create a new page
    """
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )


class PageListView(generics.ListAPIView):
    """
    To view a list of all existing pages
    """
    serializer_class = serializers.PageSerializer
    queryset = models.Page.objects.all()


class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    To view and edit a specific version of a page
    (a new version is created when editing)
    """
    serializer_class = serializers.PageSerializer
    permission_classes = (IsAdminUser, )
    queryset = models.Page.objects.all()


class VersionListView(generics.ListAPIView):
    """
    To view a list of all versions of the selected page
    """
    serializer_class = serializers.VersionSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('pk')
        versions = models.Page.history.filter(id=page_id)
        return versions


class VersionDetailView(generics.RetrieveAPIView):
    """
    To view a specific version
    """
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


class SetVersionView(generics.UpdateAPIView):
    """
    To install the current version of the selected page
    """
    serializer_class = serializers.SetVersionSerializer
    permission_classes = (IsAdminUser, )

    def get_object(self):
        pk = self.kwargs.get('pk')
        return models.Page.objects.get(id=pk)

    def update(self, request, *args, **kwargs):
        """
        Installs any selected version by history_id
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            page = self.get_object()
            version = page.history.get(
                history_id=serializer.data["history_id"]
            )
            version.instance.save_without_historical_record()
            return Response(status=200, data=serializer.data)
        return Response(status=400)