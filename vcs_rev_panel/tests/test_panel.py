from unittest.mock import MagicMock

from django.test import TestCase
from vcs_rev_panel.panels import GitRevisionPanel


class GitRevisionPanelTestCase(TestCase):
    def setUp(self):
        toolbar = MagicMock()
        self.panel = GitRevisionPanel(toolbar)

    def test_template(self):
        self.assertEqual(self.panel.template, 'git.html')
