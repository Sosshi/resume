from django.test import TestCase, SimpleTestCase
from blog.models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestDashBoardViews(SimpleTestCase):
    def test_dashboard_view(self):
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view(self):
        response = self.client.get("/dashboard/blog/")
        self.assertEqual(response.status_code, 200)

    def test_statistics_view(self):
        response = self.client.get("/dashboard/statistics/")
        self.assertEqual(response.status_code, 200)


class TestDashboardDynamicViews(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create(
            username="symon", email="symon@gmail.com", password="mwenewungu2@"
        )
        self.post = Post.objects.create(
            author=self.user,
            title="Test blog",
            subtitle="Nothing much",
            isPublished=True,
        )
