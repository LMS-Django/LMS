from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(email="admin@example.com").exists():
    User.objects.create_superuser(
        first_name="admin",
        last_name="admin",
        email="admin@example.com",
        password="admin"
    )
