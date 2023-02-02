from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="12345",
            years_of_experience=3
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="redactor12345",
            years_of_experience=3
        )

    def test_redactor_experience_listed(self):
        """Tests that redactor's years_of_experience is on redactor admin page"""
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_experience_listed(self):
        """Tests that redactor's years_of_experience is in redactor detail admin page"""
        url = reverse("admin:newspaper_redactor_change", args=[self.redactor.id])
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)
