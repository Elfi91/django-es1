from django.test import TestCase, Client
from django.urls import reverse

class ApiTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
    
    def test_users_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
