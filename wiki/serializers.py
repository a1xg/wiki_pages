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

class PageListSerializer(PageSerializer):
    pass


class PageVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = '__all__'
