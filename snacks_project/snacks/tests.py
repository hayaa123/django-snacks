from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class SnacksTests(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_aboutUs_status_code(self):
        url = reverse("about-us")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response,"home.html")
        self.assertTemplateUsed(response,"_base.html")  

    def test_aboutUs_page_template(self):
        url = reverse("about-us")
        response = self.client.get(url)
        self.assertTemplateUsed(response,"About_us.html")
        self.assertTemplateUsed(response,"_base.html")  

    