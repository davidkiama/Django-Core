from django.test import TestCase
from .models import Editor, Article, Tags

# Create your tests here.


class EditorTestClass(TestCase):
    def setUp(self):
        self.kiama = Editor(first_name='David',
                            last_name='Kiama', email='davidkiama@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.kiama, Editor))

    def test_save(self):
        self.kiama.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
