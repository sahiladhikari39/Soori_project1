from django.contrib.auth.models import UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    """
    `python manage.py createsuperuser` only ever fills in fields Django
    already knows about (username, email, password) -- it has no idea
    our `role` field exists, so it would leave it blank. A blank role
    satisfies neither branch of our CheckConstraint (blank isn't
    "soori_admin", but client is also null), so the database would
    reject the INSERT outright.

    Forcing role=soori_admin here isn't a workaround -- a Django
    superuser IS conceptually a Soori Admin in this system, so this is
    just the correct behavior.
    """

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        from .models import Role  # local import avoids a circular import at module load time

        extra_fields.setdefault("role", Role.SOORI_ADMIN)
        extra_fields["client"] = None
        return super().create_superuser(username, email, password, **extra_fields)