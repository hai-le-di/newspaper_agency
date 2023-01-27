from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator

from newspaper.models import Redactor, Newspaper
from django import forms


class RedactorCreationForm(UserCreationForm):
    MIN_VALUE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0, message="Enter a positive integer")]
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorExperienceUpdateForm(forms.ModelForm):

    MIN_VALUE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0, message="Enter a positive integer")]
    )

    class Meta:
        model = Redactor
        fields = ["years_of_experience"]

