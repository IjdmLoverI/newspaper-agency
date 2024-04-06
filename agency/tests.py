from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from agency.models import Topic, Newspaper


class IndexViewTest(TestCase):
    def setUp(self):
        # Create a redactor
        self.redactor = get_user_model().objects.create_user(
            username="testredactor", password="12345"
        )
        self.client = Client()
        topic = Topic.objects.create(name="Topic1")
        Newspaper.objects.create(
            title="Newspaper1",
            content="Content1",
            pub_date="2022-01-01T00:00Z",
            topic=topic,
        )

    def test_index_view(self):
        self.client.login(username="testredactor", password="12345")
        response = self.client.get(reverse("agency:index"))
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            self.assertEqual(response.context["num_redactors"], 1)
            self.assertEqual(response.context["num_topics"], 1)
            self.assertEqual(response.context["num_newspapers"], 1)
