from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from notes.models import Notes


class Command(BaseCommand):
    help = "Seed default groups, permissions, and users"

    def handle(self, *args, **kwargs):
        # === Ambil ContentType untuk Notes ===
        content_type = ContentType.objects.get_for_model(Notes)

        # === Ambil semua permission default Notes ===
        all_permissions = Permission.objects.filter(content_type=content_type)

        # === Buat Group: Admin ===
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        admin_group.permissions.set(all_permissions)  # semua permission Notes
        self.stdout.write(self.style.SUCCESS("✅ Group Admin sinkron dengan semua permission"))

        # === Buat Group: Editor ===
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        allowed = ["add_notes", "change_notes", "view_notes"]  # hanya sebagian
        editor_group.permissions.set(all_permissions.filter(codename__in=allowed))
        self.stdout.write(self.style.SUCCESS("✅ Group Editor sinkron dengan sebagian permission"))

        # === Buat User Admin ===
        if not User.objects.filter(username="admin").exists():
            admin_user = User.objects.create_user(
                username="admin",
                password="admin123",
                email="admin@example.com",
                is_staff=True,
                is_superuser=True,
            )
            admin_user.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS("👤 User 'admin' dibuat + masuk Admin group"))
        else:
            self.stdout.write("ℹ️ User 'admin' sudah ada")

        # === Buat User Editor ===
        if not User.objects.filter(username="editor").exists():
            editor_user = User.objects.create_user(
                username="editor",
                password="editor123",
                email="editor@example.com",
                is_staff=True,
            )
            editor_user.groups.add(editor_group)
            self.stdout.write(self.style.SUCCESS("👤 User 'editor' dibuat + masuk Editor group"))
        else:
            self.stdout.write("ℹ️ User 'editor' sudah ada")

        self.stdout.write(self.style.SUCCESS("Seeder selesai 🚀"))
