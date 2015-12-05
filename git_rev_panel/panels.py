from debug_toolbar.panels import Panel
from .client import GitClient


class GitRevisionPanel(Panel):
    title = 'Revision'

    def __init__(self, *args, **kwargs):
        self.client = GitClient()
        super().__init__(*args, **kwargs)

    def has_content(self):
        return False

    def nav_subtitle(self):
        if self.client.is_gitdir():
            return self.client.get_short_hash()
        return 'git repository is not detected'
