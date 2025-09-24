from django import forms
from notes.models import Notes
from django.core.validators import MinLengthValidator

class NoteValidation(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        validators=[MinLengthValidator(5, message="Isi catatan minimal 5 karakter")],
        error_messages={
            "required": "Isi catatan tidak boleh kosong",
        },
    )

    class Meta:
        model = Notes
        fields = ["title", "content"]
        error_messages = {
            "title": {
                "required": "Judul tidak boleh kosong",
                
            },
            "content": {
                "required": "Isi catatan tidak boleh kosong",
            },
        }