import datetime
from ..compatibility import MagicMock, PropertyMock
from django.test import TestCase

from vcs_info_panel.panels import BaseVCSInfoPanel


class BaseVCSPanelTestCase(TestCase):
    def setUp(self):
        self.toolbar = MagicMock()
        self.panel = BaseVCSInfoPanel(self.toolbar)
        self.mock_client = MagicMock()
        self.original_client = type(self.panel).client
        type(self.panel).client = PropertyMock(return_value=self.mock_client)

    def tearDown(self):
        type(self.panel).client = self.original_client

    def test_template(self):
        self.mock_client.base_command = 'vcs_name'
        self.assertEqual(self.panel.template, 'vcs_name.html')

    def test_has_content_is_true(self):
        self.panel.client.is_repository = MagicMock(return_value=True)
        self.assertEqual(self.panel.has_content, True)

    def test_has_content_is_false(self):
        self.panel.client.is_repository = MagicMock(return_value=False)
        self.assertEqual(self.panel.has_content, False)

    def test_nav_subtitle(self):
        self.panel.client.get_short_hash = MagicMock(return_value='bba82a1')
        self.assertEqual(self.panel.nav_subtitle, 'bba82a1')

    def test_nav_subtitle_with_not_git_repository(self):
        self.panel.client.is_repository = MagicMock(return_value=False)
        self.assertEqual(self.panel.nav_subtitle, 'repository is not detected')

    def test_get_stats(self):
        self.toolbar.stats = {self.panel.panel_id: {'key': 'value'}}
        self.panel.client.is_repository = MagicMock(return_value=True)
        self.panel.client.get_short_hash = MagicMock(return_value='bba82a1')
        self.panel.client.get_hash = MagicMock(return_value='bba82a1877683b98bccdee4a22d5b6ff40aaa536')
        self.panel.client.get_author_name = MagicMock(return_value='giginet')
        self.panel.client.get_author_email = MagicMock(return_value='giginet@kawaz.org')
        self.panel.client.get_author_info = MagicMock(return_value='giginet<giginet@kawaz.org>')
        self.panel.client.get_committer_name = MagicMock(return_value='giginet2')
        self.panel.client.get_committer_email = MagicMock(return_value='giginet2@kawaz.org')
        self.panel.client.get_committer_info = MagicMock(return_value='giginet2<giginet2@kawaz.org>')
        self.panel.client.get_message = MagicMock(return_value='Fix issue')
        self.panel.client.get_date = MagicMock(return_value=datetime.datetime(2015, 1, 1))
        self.panel.client.get_current_branch_name = MagicMock(return_value='master')

        stats = self.panel.get_stats()
        self.assertEqual(stats['short_hash'], 'bba82a1')
        self.assertEqual(stats['hash'], 'bba82a1877683b98bccdee4a22d5b6ff40aaa536')
        self.assertEqual(stats['author'], 'giginet<giginet@kawaz.org>')
        self.assertEqual(stats['committer'], 'giginet2<giginet2@kawaz.org>')
        self.assertEqual(stats['message'], 'Fix issue')
        self.assertEqual(stats['updated_at'], datetime.datetime(2015, 1, 1))
        self.assertEqual(stats['branch_name'], 'master')
        self.assertEqual(stats['key'], 'value')

    def test_get_stats_without_repository(self):
        self.toolbar.stats = {self.panel.panel_id: {'key': 'value'}}
        self.panel.client.is_repository = MagicMock(return_value=False)
        self.assertEqual(self.panel.get_stats(), {'key': 'value'})
