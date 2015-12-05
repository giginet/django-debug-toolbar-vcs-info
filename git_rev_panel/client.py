import os
import subprocess
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

    def _execute_git(self, main, *options):
        commands = ['git', main] + list(options)
        raw_data = subprocess.check_output(commands)
        return raw_data.decode()
