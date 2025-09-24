from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Notes as Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        # buat user dummy
        user = User.objects.create_user(username="tester", password="12345")
        
        # buat note baru
        note = Note.objects.create(
            user=user,
            title="Belajar Test",
            content="Isi catatan"
        )
        
        # cek field sesuai yang diinput
        self.assertEqual(note.title, "Belajar Test")
        self.assertEqual(note.content, "Isi catatan")
        
        # cek jumlah note di database
        self.assertEqual(Note.objects.count(), 1)


class NoteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="12345")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("notes:note_index"))
        self.assertEqual(response.status_code, 302)  # redirect ke login
        print('Response status code (not logged in):', response.status_code)

    def test_logged_in_user_can_access_notes(self):
        self.user = User.objects.create_superuser(username="testeradmin", password="12345")
        logged_in = self.client.login(username="testeradmin", password="12345")
        Note.objects.create(user=self.user, title="Catatan 1", content="Isi catatan 1") 
        response = self.client.get(reverse("notes:note_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catatan 1")  # pastikan judul note tampil
