from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profiles, loginPage, logoutPage


class TestUrls(SimpleTestCase):

    def test_url_profiles(self):
        url = reverse("profiles")
        self.assertEquals(resolve(url).func, profiles)

    def test_url_loginPage(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, loginPage)

    def test_url_logoutPage(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logoutPage)