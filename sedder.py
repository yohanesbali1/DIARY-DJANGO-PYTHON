from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from notes.models import Notes


class Command(BaseCommand):
    help = "Assign default permissions ke groups dan users"

    def handle(self, *args, **kwargs):
        # Ambil content type dari model Notes
        content_type = ContentType.objects.get_for_model(Notes)

        # Ambil permission bawaan (add, change, delete, view)
        all_permissions = Permission.objects.filter(content_type=content_type)

        # === Admin Group ===
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        admin_group.permissions.set(all_permissions)  # kasih semua
        self.stdout.write(self.style.SUCCESS("✅ Group Admin sinkron dengan semua permission"))

        # === Editor Group ===
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        allowed = ["add_notes", "change_notes", "view_notes"]
        editor_group.permissions.set(
            all_permissions.filter(codename__in=allowed)
        )
        self.stdout.write(self.style.SUCCESS("✅ Group Editor sinkron dengan sebagian permission"))

        # === Buat User dan Assign Group ===
        if not User.objects.filter(username="admin").exists():
            admin_user = User.objects.create_user(
                username="admin",
                password="admin123",
                is_staff=True,
                is_superuser=True,
            )
            admin_user.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS("👤 User admin dibuat + masuk Admin group"))

        if not User.objects.filter(username="editor").exists():
            editor_user = User.objects.create_user(
                username="editor",
                password="editor123",
                is_staff=True,
            )
            editor_user.groups.add(editor_group)
            self.stdout.write(self.style.SUCCESS("👤 User editor dibuat + masuk Editor group"))
