from django.test import TestCase
from django.shortcuts import reverse


class HomePageViewTest(TestCase):

    # test url
    def test_home_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_view_url(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_url(self):
        response = self.client.get('/pages/listing_page/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_url(self):
        response = self.client.get('/pages/detail_page/')
        self.assertEqual(response.status_code, 200)

    # test urls by name
    def test_home_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_url_by_name(self):
        response = self.client.get(reverse('listing-page'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_url_by_name(self):
        response = self.client.get(reverse('detail-page'))
        self.assertEqual(response.status_code, 200)

