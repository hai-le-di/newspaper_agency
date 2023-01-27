from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic

TOPIC_URL = reverse("newspaper:topic-list")


class PublicTopic(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopic(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123",
            years_of_experience=3,
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="name")
        Topic.objects.create(name="name_two")
        topics = Topic.objects.all()

        res = self.client.get(TOPIC_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["topic_list"]),
            list(topics)
        )
