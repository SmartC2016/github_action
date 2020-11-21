# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


class StartPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_pages_startpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_pages_startpage_contains_correct_html(self):
        self.assertContains(self.response, 'Hello')

    def test_pages_startpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page')
