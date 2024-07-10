from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создание суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('admin12345')
        user.save()
