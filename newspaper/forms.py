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


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=66,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=66,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by topic"})
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username.."})
    )