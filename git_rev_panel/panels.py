from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import Panel
from .client import GitClient


class GitRevisionPanel(Panel):
    title = _('Revision')
    template = 'revision.html'

    def __init__(self, *args, **kwargs):
        self.client = GitClient()
        super().__init__(*args, **kwargs)

    @property
    def nav_subtitle(self):
        if self.client.is_gitdir():
            return self.client.get_short_hash()
        return 'git repository is not detected'

    def get_stats(self):
        context = super().get_stats()
        context.update({
            'short_hash': self.client.get_short_hash(),
            'hash': self.client.get_hash(),
            'author': self._get_pretty_author(),
            'committer': self._get_pretty_committer(),
            'message': self.client.get_message(),
            'updated_at': self.client.get_date(),
            'branch_name': self.client.get_current_branch_name()
        })
        return context

    def _get_pretty_author(self):
        return self._pretty_name(self.client.get_author_name(),
                                 self.client.get_author_email())

    def _get_pretty_committer(self):
        return self._pretty_name(self.client.get_committer_name(),
                                 self.client.get_committer_email())

    @staticmethod
    def _pretty_name(self, name, email):
        return '{}<{}>'.format(name, email)
