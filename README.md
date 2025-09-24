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
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate database**

   ```bash
   python manage.py migrate
   ```

5. **Buat superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Jalankan server**
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Testing

Project ini sudah dilengkapi dengan unit test.  
Untuk menjalankan semua test:

```bash
python manage.py test
```

Contoh test sederhana (cek model `Note`):

```python
class NoteModelTest(TestCase):
    def test_create_note(self):
        user = User.objects.create_user(username="tester", password="12345")
        note = Note.objects.create(user=user, title="Belajar Test", content="Isi catatan")

        self.assertEqual(note.title, "Belajar Test")
        self.assertEqual(Note.objects.count(), 1)
```

## 📂 Struktur Project

```
notes/
├── migrations/
├── templates/
│   └── notes/
│       └── note_list.html
├── tests.py
├── models.py
├── views.py
├── urls.py
```

---

## 📜 Lisensi

MIT License © 2025
