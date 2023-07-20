from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Song


class MovieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Song.objects.create(
            title="song1", owner=self.user, description="description test"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "song1")

    def test_song_content(self):
        self.assertEqual(f"{self.song.title}", "song1")
        self.assertEqual(f"{self.song.owner}", "owner")
        self.assertEqual(f"{self.song.description}", "description test")

    def test_song_list_view(self):
        response = self.client.get(reverse("list_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "song1")
        self.assertTemplateUsed(response, "song-list.html")

    def test_song_detail_view(self):
        response = self.client.get(reverse("song_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Owner: owner")
        self.assertTemplateUsed(response, "song-detail.html")

    def test_song_create_view(self):
        response = self.client.post(
            reverse("create_view"),
            {
                "title": "Diva",
                "owner": self.user.id,
                "description": "test",

            }, follow=True
        )

        self.assertRedirects(response, reverse("detail_view", args="2"))
        self.assertContains(response, "Details about Song")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update_view", args="1"),
            {"title": "Updated title", "owner":self.user.id, "description":"new description"}
        )
        self.assertRedirects(response, reverse("detail_view", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("delete_view", args="1"))
        self.assertEqual(response.status_code, 200)