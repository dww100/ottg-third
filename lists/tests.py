from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "To-Do")