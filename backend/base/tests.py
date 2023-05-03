import json
from django.http import HttpRequest
from django.test import TestCase

from api.views import getAllUsers
from os.path import dirname, join

# Create your tests here.


class MessagesTestCase(TestCase):
    fixtures = ["startermodels.json"]  # Loads these starting models into our DB
    start_models = []

    @classmethod
    def setUpClass(cls):
        super(MessagesTestCase, cls).setUpClass()
        script_dir = dirname(__file__)
        rel_path = "fixtures/startermodels.json"
        abs_path = join(script_dir, rel_path)
        f = open(abs_path)
        MessagesTestCase.start_models = json.load(f)
        f.close()

    def test_get_users(self):
        # Arrange
        ian = {"id": "Ian"}
        for obj in MessagesTestCase.start_models:
            if obj["pk"] == "Ian":
                ian.update(obj["fields"])

        expectedResponse = [ian]
        request = HttpRequest()
        request.method = "GET"

        # Act
        response = getAllUsers(request)
        response = [dict(response.data[0])]  # type: ignore

        # Assert
        self.assertEqual(len(expectedResponse), len(response))
        self.assertEqual(
            sorted(expectedResponse[0].items()), sorted(response[0].items())
        )
