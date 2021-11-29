from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from wiki.models import *
from wiki.serializers import *


class PageCreateViewTest(APITestCase):
    def test_post(self):
        pass


class PageListViewTest(APITestCase):
    def test_get(self):
        page_1 = Page.objects.create(title='Test title 1', text='Test content 1')
        page_2 = Page.objects.create(title='Test title 2', text='Test content 2')
        page_3 = Page.objects.create(title='Test title 3', text='Test content 3')
        serializer_data = PageSerializer([page_1, page_2, page_3], many=True).data

        url = '/api/v1/pages/list'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class PageDetailViewTest(APITestCase):
    def test_get(self):
        pass


class VersionListViewTest(APITestCase):
    def test_get(self):
        pass


class VersionDetailViewTest(APITestCase):
    def test_get(self):
        pass


class SetVersionViewTest(APITestCase):
    def test_put(self):
        pass