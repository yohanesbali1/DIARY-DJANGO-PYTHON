from django import forms
from notes.models import Note

class NoteValidation(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
        error_messages = {
            "title": {
                "required": "Judul tidak boleh kosong",
                "max_length": "Judul terlalu panjang",
            },
            "content": {
                "required": "Isi catatan tidak boleh kosong",
            },
        }