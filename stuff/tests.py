from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Stuff


class StuffTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(
            username="testuser", password="pass"
        )
        testuser.save()

        test_stuff = Stuff.objects.create(
            name="boat",
            owner=testuser,
            description="Water car",
        )
        test_stuff.save()

    def test_stuff_model(self):
        stuff = Stuff.objects.get(id=1)
        actual_owner = str(stuff.owner)
        actual_name = str(stuff.name)
        actual_description = str(stuff.description)
        self.assertEqual(actual_owner, "testuser")
        self.assertEqual(actual_name, "boat")
        self.assertEqual(actual_description, "Water car")

    def test_get_stuff_list(self):
        url = reverse("stuff_list")
        self.client.login(username='testuser', password="pass")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stuff = response.data
        self.assertEqual(len(stuff), 1)
        self.assertEqual(stuff[0]["name"], "boat")

    def test_get_stuff_by_id(self):
        url = reverse("stuff_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stuff = response.data
        self.assertEqual(stuff["name"], "boat")

    def test_create_stuff(self):
        url = reverse("stuff_list")
        data = {"owner": 1, "name": "car", "description": "Drives on the road"}
        self.client.login(username='testuser', password="pass")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        stuff = Stuff.objects.all()
        self.assertEqual(len(stuff), 2)
        self.assertEqual(stuff.get(id=2).name, "car")

    def test_update_stuff(self):
        url = reverse("stuff_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "scooter",
            "description": "Much smaller car, far less power",
        }
        self.client.login(username='testuser', password="pass")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stuff = Stuff.objects.get(id=1)
        self.assertEqual(stuff.name, data["name"])
        self.assertEqual(stuff.owner.id, data["owner"])
        self.assertEqual(stuff.description, data["description"])

    def test_delete_stuff(self):
        url = reverse("stuff_detail", args=(1,))
        self.client.login(username='testuser', password="pass")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        stuff = Stuff.objects.all()
        self.assertEqual(len(stuff), 0)