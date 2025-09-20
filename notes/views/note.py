from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from notes.models import Notes
from notes.validation.note_validation import NoteValidation

@login_required
def index(request):
    print("masuk index")
    notes = Notes.objects.filter(user=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})

@login_required
def create(request):
    if request.method == "POST":
        form = NoteValidation(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_index")
    else:
        form = NoteValidation()
    return render(request, "notes/note_form.html", {"form": form})

@login_required
def edit(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteValidation(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_index")
    else:
        form = NoteValidation(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "note": note})

@login_required
def delete(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("note_index")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
