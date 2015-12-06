from django.test import TestCase

from vcs_info_panel.clients.git import GitClient


class GitClientTestCase(TestCase):
    def setUp(self):
        self.client = GitClient()

    def test_base_command(self):
        self.assertEqual(self.client.base_command, 'git')
