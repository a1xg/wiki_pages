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
        # fields = (
        #    'id',
        #    'history_id',
        #    'text',
        #    'created',
        #    'history_date',
        # )
        fields = '__all__'
