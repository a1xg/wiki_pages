from datetime import datetime

from django.test import TestCase
from wiki.models import *
from wiki.serializers import *


class PageSerializerTest(TestCase):
    def test_ok(self):
        page_1 = Page.objects.create(title='Test title 1', text='Test content 1')
        page_2 = Page.objects.create(title='Test title 2', text='Test content 2')
        page_3 = Page.objects.create(title='Test title 3', text='Test content 3')
        serializer_data = PageSerializer([page_1, page_2, page_3], many=True).data
        expected_data = [
            {
                'id': page_1.id,
                'title': 'Test title 1',
                'text': 'Test content 1',
                'created': page_1.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            },
            {
                'id': page_2.id,
                'title': 'Test title 2',
                'text': 'Test content 2',
                'created': page_2.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            },
            {
                'id': page_3.id,
                'title': 'Test title 3',
                'text': 'Test content 3',
                'created': page_3.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            },
        ]
        self.assertEqual(expected_data, serializer_data)


class VersionSerializerTest(TestCase):
    def test_ok(self):
        # create page
        page = Page.objects.create(
            title='Test title(original)',
            text='Test content(original)'
        )
        # create new versions of page
        page.history.create(
            id=page.id,
            created=page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            title='Test title(edit1)',
            text='Test content(edit1)',
            history_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        )
        page.history.create(
            id=page.id,
            created=page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            title='Test title(edit2)',
            text='Test content(edit2)',
            history_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        )
        all_versions = page.history.all().order_by('history_id')
        serializer_data = VersionSerializer(all_versions, many=True).data

        expected_data = [
            {
                'history_id': all_versions[0].history_id,
                'id': page.id,
                'title': 'Test title(original)',
                'text': 'Test content(original)',
                'created': page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'history_date': all_versions[0].history_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'history_change_reason': None,
                'history_type': '+',
                'history_user': None,
            },
            {
                'id': page.id,
                'history_id': all_versions[1].history_id,
                'created': page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'history_date': all_versions[1].history_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'title': 'Test title(edit1)',
                'text': 'Test content(edit1)',
                'history_change_reason': None,
                'history_type': '',
                'history_user': None,
            },
            {
                'id': page.id,
                'history_id': all_versions[2].history_id,
                'created': page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'history_date': all_versions[2].history_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'title': 'Test title(edit2)',
                'text': 'Test content(edit2)',
                'history_change_reason': None,
                'history_type': '',
                'history_user': None,
            },
        ]

        self.assertEqual(expected_data, serializer_data)


class SetVersionSerializerTest(TestCase):
    def test_ok(self):
        data = {'history_id': 6}
        serializer_data = SetVersionSerializer(data).data
        expected_data = {'history_id': 6}
        self.assertEqual(serializer_data, expected_data)