from rest_framework import serializers
from . import models


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = (
            'id',
            'title',
            'text',
            'created',
        )


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page.history.model
        fields = '__all__'
