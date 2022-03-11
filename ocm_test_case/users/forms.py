from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django import forms

from django.conf import settings

from ocm_test_case.users.models import UserEmails

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserEmailForm(forms.Form):

    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(UserEmailForm, self).__init__(*args, **kwargs)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        to_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = cl_data.get('message')

        return subject, msg, to_email

    def send(self):

        subject, msg, to_email = self.get_info()

        answ = send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email]
        )

        UserEmails.objects.create(destination=to_email, status=bool(answ),
                                  mes_title=subject, mes_text=msg, user_id=self.request.user)


class UserEmailsListForm(forms.Form):
    class Meta:
        model = UserEmails
        fields = ["destination", 'mes_title', 'mes_text', 'status']


class UserEmailEditForm(forms.ModelForm):

    class Meta:
        model = UserEmails
        fields = ["destination", 'mes_title', 'mes_text', 'status']
