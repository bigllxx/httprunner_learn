# coding: utf-8
# author: bigllxx@163.com
import requests
from .base import ApiServerUnittest


class TestApiServer(ApiServerUnittest):
    def setUp(self):
        super(TestApiServer, self).setUp()
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()

    def tearDown(self):
        super(TestApiServer, self).tearDown()

    def test_create_user_not_existed(self):

        url = "%s/api/users/%d" % (self.host, 1000)
        data = {
            "name": "user1",
            "password": "123456"
        }
        resp = self.api_client.post(url, json=data)

        self.assertEqual(201, resp.status_code)
        self.assertEqual(True, resp.json()["success"])
