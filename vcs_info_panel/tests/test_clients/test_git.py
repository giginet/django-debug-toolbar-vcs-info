import subprocess
from unittest.mock import patch
from django.test import TestCase

from vcs_info_panel.clients.git import GitClient


class GitClientTestCase(TestCase):
    def setUp(self):
        self.client = GitClient()

    def _test_called_check_output(self, commands):
        with patch('subprocess.check_output') as _check_output:
            _check_output.assert_called_with(commands)

    def test_base_command(self):
        self.assertEqual(self.client.base_command, 'git')

    def test_is_repository_with_repository(self):
        with patch('subprocess.check_output') as _check_output:
            _check_output.return_value = b'true'
            self.assertEqual(self.client.is_repository(), True)
            _check_output.assert_called_once_with(['git', 'rev-parse', '--is-inside-work-tree'])

    def _patch_without_repository(self, func):
        with patch('subprocess.check_output') as _check_output:
            _check_output.side_effect = subprocess.CalledProcessError(128,
                                                                     ['git', 'rev-parse', '--is-inside-work-tree'],
                                                                     'fatal: Not a git repository (or any of the parent directories): .git')

    def test_is_repository_without_repository(self):
        def _func(_check_output):
            self.assertEqual(self.client.is_repository(), False)
            _check_output.assert_called_once_with(['git', 'rev-parse', '--is-inside-work-tree'])
        self._patch_without_repository(_func)
