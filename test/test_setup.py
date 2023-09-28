from rest_framework.test import APITestCase
from rest_framework import status

from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self):
        from core.users.models import Users
        faker = Faker()

        self.login_url = '/login/'

        self.user = Users.objects.create_superuser(
            username='dev',
            email='dev@gmail.com',
            name='dev',
            password='dev'
        )

        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'email': self.user.email,
                'name': self.user.name,
                'password': 'dev',
            },
            format='json'
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        return super().setUp()

