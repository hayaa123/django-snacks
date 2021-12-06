from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase,TestCase
from django.urls import reverse
# Create your tests here.
class SnacksTests(TestCase):
    def test_home_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_aboutUs_status_code(self):
        url = reverse("about-us")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snack_list_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    # def test_snack_detail_status_code(self):
    #     url = reverse("snack_detail")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,200)

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

    def test_snack_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response,"snack_list.html")
        self.assertTemplateUsed(response,"_base.html") 

    # def test_snack_detail_page_template(self):
    #     url = reverse("snack_detail")
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response,"snack_detail.html")
    #     self.assertTemplateUsed(response,"_base.html")  

    