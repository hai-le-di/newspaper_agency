from datetime import datetime

from django.test import TestCase

from newspaper.models import Redactor, Newspaper, Topic


class ModelsTests(TestCase):

    def test_topic_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic), "test")

    def test_redactor_str(self):
        redactor = Redactor.objects.create(username="test",
                                           password="12345",
                                           first_name="test first",
                                           last_name="test last",
                                           years_of_experience=3)
        self.assertEqual(str(redactor), "test (test first test last)")

    def test_newspaper_str(self):
        published_date = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(title="test",
                                             content="test content",
                                             published_date=published_date,
                                             topic=topic,
                                             )
        self.assertEqual(
            str(newspaper), f"{newspaper.title} ({newspaper.topic},"
                            f" {newspaper.published_date})"
        )
