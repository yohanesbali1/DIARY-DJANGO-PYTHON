# 📝 Django Notes App

Project ini adalah aplikasi catatan sederhana menggunakan **Django**.
Fitur utama:

- Autentikasi user (login/logout).
- User biasa hanya bisa melihat catatannya sendiri.
- Superuser bisa melihat semua catatan.
- Unit test dengan `django.test.TestCase`.

---

## 🚀 Instalasi & Setup

1. **Clone repo**

   ```bash
   git clone https://github.com/yohanesbali1/diary-django-python.git
   cd diary-django-python
   ```

2. **Buat virtual environment & aktifkan**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate database**

   ```bash
   python manage.py migrate
   ```

5. **Jalankan seeder untuk data awal**

   Seeder akan otomatis membuat user:

   - **Superadmin**: username `admin`, password `admin123`
   - **Editor**: username `editor`, password `editor123`

   ```bash
   python manage.py seed_data
   ```

6. **Buat superuser (opsional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Jalankan server**

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Testing

Project ini sudah dilengkapi dengan unit test menggunakan Django `TestCase`.
Untuk menjalankan semua test:

```bash
python manage.py test
```

Contoh test yang tersedia:

- **NoteModelTest**: Menguji pembuatan note dan validasi field.
- **NoteViewTest**: Menguji akses view:

  - Redirect jika belum login.
  - Superuser dapat melihat semua catatan.

Contoh test sederhana:

```python
class NoteModelTest(TestCase):
    def test_create_note(self):
        user = User.objects.create_user(username="tester", password="12345")
        note = Note.objects.create(user=user, title="Belajar Test", content="Isi catatan")

        self.assertEqual(note.title, "Belajar Test")
        self.assertEqual(note.content, "Isi catatan")
        self.assertEqual(Note.objects.count(), 1)
```

---

## 📜 Lisensi

MIT License © 2025
