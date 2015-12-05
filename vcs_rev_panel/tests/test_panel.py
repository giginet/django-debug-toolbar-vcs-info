from django.test import TestCase


class RevisionPanelTestCase(TestCase):
    def setUp(self):
        self.panel = RevisionPanel()
