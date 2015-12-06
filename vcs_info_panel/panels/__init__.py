from ..clients.git import GitClient
from .base import BaseVCSInfoPanel


class GitInfoPanel(BaseVCSInfoPanel):
    client_class = GitClient
