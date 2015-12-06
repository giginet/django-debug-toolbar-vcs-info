from subprocess import CalledProcessError
from .base import BaseVCSClient


class GitClient(BaseVCSClient):
    base_command = 'git'
    ISO_FORMAT = '%Y-%m-%d %H:%M:%S'

    def is_repository(self):
        try:
            is_work_dir = self._execute_vcs('rev-parse', '--is-inside-work-tree')
            return is_work_dir.startswith('true')
        except CalledProcessError:
            return False

    def get_hash(self):
        return self._execute_vcs('rev-parse', 'HEAD')

    def get_short_hash(self):
        return self._execute_vcs('rev-parse', '--short', 'HEAD')

    def get_current_branch_name(self):
        return self._execute_vcs('rev-parse', '--abbrev-ref', 'HEAD')

    def get_author_name(self):
        return self._execute_vcs_show('%an')

    def get_author_email(self):
        return self._execute_vcs_show('%ae')

    def get_committer_name(self):
        return self._execute_vcs_show('%cn')

    def get_committer_email(self):
        return self._execute_vcs_show('%ce')

    def get_date(self):
        iso_format = self._execute_vcs_show('%ci')
        try:
            return datetime.datetime.strptime(iso_format, self.ISO_FORMAT)
        except:
            return None

    def get_message(self):
        return self._execute_vcs_show('%b')

    def _execute_vcs_show(self, format_text, hash='HEAD'):
        return self._execute_vcs('show', '--format={}'.format(format_text), hash).strip()
