from dateutil.parser import parse
from .base import BaseVCSClient, returns_on_fail


class GitClient(BaseVCSClient):
    base_command = 'git'

    @returns_on_fail(False)
    def is_repository(self):
        is_work_dir = self._execute_vcs('rev-parse', '--is-inside-work-tree')
        return is_work_dir.startswith('true')

    @returns_on_fail(None)
    def get_hash(self):
        return self._execute_vcs('rev-parse', 'HEAD')

    @returns_on_fail(None)
    def get_short_hash(self):
        return self._execute_vcs('rev-parse', '--short', 'HEAD')

    @returns_on_fail(None)
    def get_current_branch_name(self):
        return self._execute_vcs('rev-parse', '--abbrev-ref', 'HEAD')

    @returns_on_fail(None)
    def get_author_name(self):
        return self._execute_vcs_show('%an')

    @returns_on_fail(None)
    def get_author_email(self):
        return self._execute_vcs_show('%ae')

    @returns_on_fail(None)
    def get_committer_name(self):
        return self._execute_vcs_show('%cn')

    @returns_on_fail(None)
    def get_committer_email(self):
        return self._execute_vcs_show('%ce')

    @returns_on_fail(None)
    def get_date(self):
        iso_format = self._execute_vcs_show('%ci')
        try:
            return parse(iso_format)
        except:
            return None

    @returns_on_fail(None)
    def get_subject(self):
        return self._execute_vcs_show('%s')

    @returns_on_fail(None)
    def get_body(self):
        return self._execute_vcs_show('%b')

    @returns_on_fail(None)
    def get_message(self):
        subject = self.get_subject()
        body = self.get_body()
        if not subject or not body:
            return None
        return '\n'.join([subject, body])

    def _execute_vcs_show(self, format_text, hash='HEAD'):
        return self._execute_vcs('show', '--format={}'.format(format_text), hash).strip()
