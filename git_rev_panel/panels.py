from debug_toolbar.panels import Panel
from .client import GitClient


class GitRevisionPanel(Panel):
    title = 'Revision'
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
            'hash': self.client.get_hash()
        })
        print(context)
        return context
