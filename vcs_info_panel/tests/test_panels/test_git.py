from ..compatibility import MagicMock

from django.template.loader import render_to_string
from django.test import TestCase

from vcs_info_panel.clients.git import GitClient
from vcs_info_panel.panels import GitInfoPanel


class GitInfoPanelTestCase(TestCase):
    def setUp(self):
        self.toolbar = MagicMock()
        self.panel = GitInfoPanel(self.toolbar)

    def test_client_class(self):
        self.assertEqual(self.panel.client_class, GitClient)

    def test_content(self):
        rendered = render_to_string('git.html')
        self.assertEqual(self.panel.client.base_command, 'git')
        self.assertEqual(self.panel.content, rendered)
