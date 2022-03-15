from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, TextField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for OCM test case.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UserEmails(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    destination = CharField(_("Destination"), max_length=64)
    mes_title = CharField(_("Title"), blank=True, max_length=255)
    mes_text = TextField(_("Message text"), blank=True)
    status = BooleanField(_("Delivered status"), default=True)

    def __repr__(self):
        return f'{self.mes_title} | {self.destination}'
