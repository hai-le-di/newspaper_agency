from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper
NEWSPAPER_LIST_URL = reverse("newspaper:newspaper-list")


class PrivateNewspaper(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123",
            years_of_experience=3
        )
        self.client.force_login(self.user)

    def test_search_newspaper(self):
        published_date = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
        topic = Topic.objects.create(name="name")
        Newspaper.objects.create(
            title="test",
            content="test content",
            published_date=published_date,
            topic=topic,
        )
        Newspaper.objects.create(
            title="test two",
            content="test content two",
            published_date=published_date,
            topic=topic,
        )
        search_data = {"model": "test"}
        resp = self.client.get(NEWSPAPER_LIST_URL, data=search_data)
        newspaper = Newspaper.objects.filter(title__icontains="test")

        self.assertEqual(
            list(resp.context["newspaper_list"]),
            list(newspaper)
        )
