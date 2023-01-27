from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic

TOPIC_LIST_URL = reverse("newspaper:topic-list")


class PrivateTopic(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="admin12345",
            years_of_experience=3
        )

        self.client.force_login(self.user)

    def test_topic_search(self):
        Topic.objects.create(name="test")
        Topic.objects.create(name="test two")
        Topic.objects.create(name="test three")

        searching_data = {"name": "test"}
        resp = self.client.get(TOPIC_LIST_URL, data=searching_data)
        topics = Topic.objects.filter(
            name__icontains="test"
        )
        self.assertEqual(
            list(resp.context["topic_list"]),
            list(topics)
        )
