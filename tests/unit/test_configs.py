import unittest

from algoliasearch.configs import SearchConfig
from algoliasearch.http.hosts import HostsCollection


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_app_id(self):
        self.assertEqual(self.config.app_id, 'foo')

    def test_api_key(self):
        self.assertEqual(self.config.api_key, 'bar')

    def test_read_timeout(self):
        self.assertEqual(self.config.read_timeout, 5)

    def test_write_timeout(self):
        self.assertEqual(self.config.write_timeout, 5)

    def test_connect_timeout(self):
        self.assertEqual(self.config.connect_timeout, 5)

    def test_wait_task_time_before_retry(self):
        self.assertEqual(self.config.wait_task_time_before_retry, 100000)


class TestSearchConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_hosts(self):
        self.assertIsInstance(self.config.hosts['write'], HostsCollection)
        self.assertIsInstance(self.config.hosts['read'], HostsCollection)

        # Assert that hosts here assigned.
        self.assertNotEqual(len(self.config.hosts['write']._hosts), 0)
        self.assertNotEqual(len(self.config.hosts['read']._hosts), 0)