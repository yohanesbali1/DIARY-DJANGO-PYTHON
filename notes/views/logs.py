from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from notes.models import AdminLog

@login_required
def log_list(request):
    logs = AdminLog.objects.all()[:100]  # tampilkan 100 log terakhir
    return render(request, "logs/log_list.html", {"logs": logs})
