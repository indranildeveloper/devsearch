from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "First name",
                "placeholder": "Enter First Name",
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Last name",
                "placeholder": "Enter Last Name",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Email address",
                "placeholder": "Enter Email id",
                "type": "email",
            }
        )
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Username",
                "placeholder": "Enter Username",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Password",
                "placeholder": "Enter Password",
                "type": "password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Password confirmation",
                "placeholder": "Confirm Password",
                "type": "password",
            }
        )
