from django.test import TestCase
from wiki.models import Page


class PageModelTest(TestCase):
    def test_create_page(self):
        page = Page.objects.create(title='Test', text='Test')
        expected_data = {'title': 'Test', 'text': 'Test'}
        self.assertEqual(expected_data['title'], page.title)
        self.assertEqual(expected_data['text'], page.text)


    def test_get_page(self):
        page = Page.objects.create(title='Test', text='Test')
        page1 = Page.objects.get(id=page.id)
        self.assertEqual(page1.title, page.title)
