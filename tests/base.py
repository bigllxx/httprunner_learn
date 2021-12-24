# coding: utf-8
# author: bigllxx@163.com
import multiprocessing
import time
import unittest
import os

from tests import api_server


def run_app():
    api_server.app.run()


class ApiServerUnittest(unittest.TestCase):
    """
    Test case class that sets up an HTTP server which can be used within the tests
    """

    @classmethod
    def setUpClass(cls):
        cls.api_server_process = multiprocessing.Process(
            target=run_app
        )
        cls.api_server_process.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()

    def test_a(self):
        print(4444)
