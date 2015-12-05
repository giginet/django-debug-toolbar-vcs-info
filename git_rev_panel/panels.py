from debug_toolbar.panels import Panel


class GitRevisionPanel(Panel):
    title = 'Revision'

    def has_content(self):
        return False
