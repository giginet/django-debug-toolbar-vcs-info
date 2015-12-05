import os
import subprocess
import dateutil.parser as parser
from subprocess import CalledProcessError


class GitClient(object):
    def is_gitdir(self):
        try:
            is_work_dir = self._execute_git('rev-parse', '--is-inside-work-tree')
            return is_work_dir.startswith('true')
        except CalledProcessError:
            return False

    def get_cwd(self):
        return os.getcwd()

    def get_hash(self):
        return self._execute_git('rev-parse', 'HEAD')

    def get_short_hash(self):
        return self._execute_git('rev-parse', '--short', 'HEAD')

    def get_current_branch_name(self):
        return self._execute_git('rev-parse', '--abbrev-ref', 'HEAD')

    def get_author_name(self):
        return self._execute_git_show('%an')

    def get_author_email(self):
        return self._execute_git_show('%ae')

    def get_committer_name(self):
        return self._execute_git_show('%cn')

    def get_committer_email(self):
        return self._execute_git_show('%ce')

    def get_date(self):
        iso_format = self._execute_git_show('%ci')
        try:
            return parser.parse(iso_format)
        except:
            return None

    def get_message(self):
        return self._execute_git_show('%b')

    @staticmethod
    def _execute_git(main, *options):
        commands = ['git', main] + list(options)
        raw_data = subprocess.check_output(commands)
        return raw_data.decode()

    def _execute_git_show(self, format, hash='HEAD'):
        return self._execute_git('show', '--format={}'.format(format), hash).strip()
