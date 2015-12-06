from unittest.mock import MagicMock

from django.test import TestCase
from vcs_info_panel.panels import GitInfoPanel


class GitInfoPanelTestCase(TestCase):
    def setUp(self):
        toolbar = MagicMock()
        self.panel = GitInfoPanel(toolbar)

    def test_template(self):
        self.assertEqual(self.panel.template, 'git.html')
