from rest_framework import serializers
from . import models


class WikiPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WikiPage
        fields = '__all__'


class VersionPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PageVersion
        fields = '__all__'
