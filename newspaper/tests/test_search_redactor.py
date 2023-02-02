from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Redactor


REDACTOR_LIST_URL = reverse("newspaper:redactor-list")


class PrivateRedactor(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_two",
            password="test12345",
            years_of_experience=3,
        )

        self.client.force_login(self.user)

    def test_search_redactor(self):
        get_user_model().objects.create_user(
            username="test",
            password="test12345",
            years_of_experience=3
        )

        get_user_model().objects.create_user(
            username="new_test",
            password="test12345",
            years_of_experience=3
        )

        search_data = {"username": "test"}
        resp = self.client.get(REDACTOR_LIST_URL, data=search_data)
        redactor = Redactor.objects.filter(username__icontains="test")

        self.assertEqual(
            list(resp.context["redactor_list"]),
            list(redactor))
