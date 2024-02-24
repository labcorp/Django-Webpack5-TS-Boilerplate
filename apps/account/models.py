from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.core.models import AbstractBaseModel


class User(AbstractBaseModel, AbstractUser):
    email = models.EmailField(_('email address'), unique=True, null=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    @property
    def display_name(self):
        return self.get_full_name() or self.username

    def __str__(self):
        return self.display_name


class Profile(AbstractBaseModel):
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(_('birthdate'), null=True, blank=True)
    optin = models.BooleanField(_('opt-out'), default=False)

    def __str__(self):
        return self.user.display_name
        