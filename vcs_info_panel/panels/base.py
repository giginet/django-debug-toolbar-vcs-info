from debug_toolbar.panels import Panel
from django.utils.translation import ugettext_lazy as _


class BaseVCSInfoPanel(Panel):
    title = _('Revision')
    _cached_client = None

    @property
    def client_class(self):
        raise NotImplementedError

    @property
    def client(self):
        if not self._cached_client:
            self._cached_client = self.client_class()
        return self._cached_client

    @property
    def nav_subtitle(self):
        if self.client.is_repository():
            return self.client.get_short_hash()
        return 'repository is not detected'

    @property
    def has_content(self):
        return self.client.is_repository()

    @property
    def template(self):
        return '{}.html'.format(self.client.base_command)

    def get_stats(self):
        context = super(BaseVCSInfoPanel, self).get_stats()
        if self.client.is_repository():
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
    def _pretty_name(name, email):
        return '{}<{}>'.format(name, email)
