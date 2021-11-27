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


class PageVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page.history.model
        fields = (
            'history_id',
            'text',
            'created',
            'history_date',
        )
