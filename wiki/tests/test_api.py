from django.contrib.auth import get_user_model
from datetime import datetime
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from wiki.models import Page
from wiki.serializers import PageSerializer, VersionSerializer


class PageCreateViewTest(APITestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            "admin",
            "admin@admin.com",
            "admin"
        )
        self.client.login(username='admin', password='admin')

    def test_create_page(self):
        data = {
            'title': 'test title',
            'text': 'test content'
        }
        url = '/api/v1/create'

        response = self.client.post(
            path=url,
            data=data,
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class PageListViewTest(APITestCase):
    def test_get(self):
        page_1 = Page.objects.create(
            title='Test title 1',
            text='Test content 1'
        )
        page_2 = Page.objects.create(
            title='Test title 2',
            text='Test content 2'
        )
        page_3 = Page.objects.create(
            title='Test title 3',
            text='Test content 3'
        )
        serializer_data = PageSerializer(
            [page_1, page_2, page_3],
            many=True
        ).data

        url = '/api/v1/pages/list'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class PageDetailViewTest(APITestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            "admin",
            "admin@admin.com",
            "admin"
        )
        self.client.login(username='admin', password='admin')

    def test_get_page(self):
        test_page = Page.objects.create(
            title='Test title',
            text='Test content'
        )
        serializer_data = PageSerializer(test_page, many=False).data

        url = f'/api/v1/pages/{test_page.id}'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_update_page(self):
        page = Page.objects.create(
            title='Test title',
            text='Test content'
        )
        new_version = {
            'title': 'updated title',
            'text': 'updated text'
        }
        url = f'/api/v1/pages/{page.id}'
        # update page
        response = self.client.put(
            path=url,
            data=new_version,
            content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(new_version['title'], response.data['title'])
        self.assertEqual(new_version['text'], response.data['text'])


class VersionListViewTest(APITestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            "admin",
            "admin@admin.com",
            "admin"
        )
        self.client.login(username='admin', password='admin')

    def test_get_list_of_versions_of_pages(self):
        page = Page.objects.create(title='Test title 1', text='Test content 1')
        # create two new versions
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
        url = f'/api/v1/pages/{page.id}/versions/list'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 3)


class VersionDetailViewTest(APITestCase):
    def test_get_version_of_page(self):
        page = Page.objects.create(title='Test title 1', text='Test content 1')
        # create new version
        page.history.create(
            id=page.id,
            created=page.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            title='Test title(edit1)',
            text='Test content(edit1)',
            history_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        )
        all_versions = page.history.all()
        serializer_data = VersionSerializer(all_versions, many=True).data
        url = f'/api/v1/pages/{page.id}/versions/' \
              f'{serializer_data[0]["history_id"]}'
        response = self.client.get(url)
        # We compare the available versions with the one received from API
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(
            serializer_data[0]['title'],
            response.data['title']
        )
        self.assertNotEqual(
            serializer_data[1]['title'],
            response.data['title']
        )


class SetVersionViewTest(APITestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            "admin",
            "admin@admin.com",
            "admin"
        )
        self.client.login(username='admin', password='admin')

    def test_set_selected_version(self):
        page = Page.objects.create(title='Test title 1', text='Test content 1')
        # create two new versions
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

        # Three versions: original, and 2 edited
        all_versions = page.history.all()
        serializer_data = VersionSerializer(all_versions, many=True).data

        # Setting an older version of the page
        put_url = f'/api/v1/pages/{page.id}/versions/set-current'
        data = {'history_id': serializer_data[1]['history_id']}
        put_response = self.client.put(
            put_url,
            data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, put_response.status_code)
        self.assertEqual(put_response.data['history_id'], data['history_id'])

        # Getting the actual page
        get_url = f'/api/v1/pages/{page.id}'
        get_response = self.client.get(get_url)
        self.assertEqual(status.HTTP_200_OK, get_response.status_code)

        # Check if the old version is installed
        self.assertEqual(
            get_response.data['title'],
            serializer_data[1]['title']
        )
        self.assertEqual(
            get_response.data['text'],
            serializer_data[1]['text']
        )
