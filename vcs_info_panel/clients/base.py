import os
import subprocess


def returns_on_fail(return_value):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except subprocess.CalledProcessError:
                return return_value
        return inner
    return decorator


class BaseVCSClient(object):
    @property
    def base_command(self):
        raise NotImplementedError

    def is_repository(self):
        raise NotImplementedError

    def get_hash(self):
        raise NotImplementedError

    def get_short_hash(self):
        raise NotImplementedError

    def get_current_branch_name(self):
        raise NotImplementedError

    def get_author_name(self):
        raise NotImplementedError

    def get_author_email(self):
        raise NotImplementedError

    def get_author_info(self):
        raise NotImplementedError

    def get_committer_name(self):
        raise NotImplementedError

    def get_committer_email(self):
        raise NotImplementedError

    def get_committer_info(self):
        raise NotImplementedError

    def get_date(self):
        raise NotImplementedError

    def get_message(self):
        raise NotImplementedError

    def _get_cwd(self):
        return os.getcwd()

    def _execute_vcs(self, main, *options):
        commands = [self.base_command, main] + list(options)
        raw_data = subprocess.check_output(commands)
        return raw_data.decode()
