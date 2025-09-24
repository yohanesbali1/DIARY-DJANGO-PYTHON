from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from notes.models import Notes,AdminLog
from django.http import JsonResponse
from notes.validation.note_validation import NoteValidation
from notes.utils import get_client_ip
from django.db import transaction
from django.contrib import messages

@login_required
@permission_required("notes.view_notes", raise_exception=True)
def index(request):
    notes = Notes.objects.filter(user=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})

@login_required
@permission_required("notes.add_notes", raise_exception=True)
def create(request):
    if request.method == "POST":
        form = NoteValidation(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # simpan note
                    note = form.save(commit=False)
                    note.user = request.user
                    note.save()

                    # catat log
                    AdminLog.objects.create(
                        user=request.user,
                        action="create",
                        model_name="Notes",
                        object_id=note.id,
                        description=f"Created note {note.title}",
                        ip_address=get_client_ip(request)
                    )

                return redirect("notes:note_index")

            except Exception as e:
              messages.error(request, f"Gagal menyimpan catatan: {str(e)}")
           

    else:
        form = NoteValidation()

    return render(request, "notes/note_form.html", {"form": form})
@login_required
@permission_required("notes.change_notes", raise_exception=True)
def edit(request, note_id):
    note = get_object_or_404(Notes, id=note_id, user=request.user)
    if request.method == "POST":
        form = NoteValidation(request.POST, instance=note)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # simpan note
                    form.save()

                    # catat log
                    AdminLog.objects.create(
                        user=request.user,
                        action="update",
                        model_name="Notes",
                        object_id=note.id,
                        description=f"Updated note dengan id {note.id}",
                        ip_address=get_client_ip(request)
                    )

                return redirect("notes:note_index")

            except Exception as e:
              messages.error(request, f"Gagal mengubah catatan")
    else:
        form = NoteValidation(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "note": note})

@login_required
@permission_required("notes.delete_notes", raise_exception=True)
def delete(request, note_id):
    note = get_object_or_404(Notes, id=note_id, user=request.user)
    if request.method == "DELETE":
        try:
            with transaction.atomic():
                    # simpan note
                    note_id = note.id
                    note_title = note.title
                    note.delete()

                    # catat log
                    AdminLog.objects.create(
                        user=request.user,
                        action="delete",
                        model_name="Notes",
                        object_id=note_id,
                        description=f"Deleted note {note_title} dengan id {note_id}",
                        ip_address=get_client_ip(request)
                    )

            return JsonResponse({"success": True, "message": "Note deleted"})

        except Exception as e:
              messages.error(request, f"Gagal menghapus catatan")
              
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)
