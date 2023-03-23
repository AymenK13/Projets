from django.test import TestCase
from .models import Company, Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='Test Company',
            city='Test City'
        )

    def test_add_note_to_company(self):
        note = Note.objects.create(text='Test note')
        self.company.notes.add(note)
        self.assertEqual(self.company.notes.first(), note)
