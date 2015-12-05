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

    def get_current_branch_name(self):
        return self._execute_git('rev-parse', '--abbrev-ref', 'HEAD')

    @staticmethod
    def _execute_git(main, *options):
        commands = ['git', main] + list(options)
        raw_data = subprocess.check_output(commands)
        return raw_data.decode()
