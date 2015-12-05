from ..clients.git import GitClient
from .base import BaseVCSRevisionPanel


class GitRevisionPanel(BaseVCSRevisionPanel):
    client_class = GitClient
