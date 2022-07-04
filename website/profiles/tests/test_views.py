from audioop import reverse
from django.test import TestCase, Client
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json

class TestViews(TestCase):

    def test_get_profiles(self):
        client = Client()
        response = client.get(reverse('profiles'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "../../templates/profiles/profiles.html")