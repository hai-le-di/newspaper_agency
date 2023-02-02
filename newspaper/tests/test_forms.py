from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import RedactorCreationForm


class FormsTests(TestCase):
    def test_redactor_creation_form_with_experience_is_valid(self):
        form_data = {
            "username": "user_name",
            "password1": "3134test",
            "password2": "3134test",
            "first_name": "first name",
            "last_name": "last name",
            "years_of_experience": 3,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_years_of_experience_is_integer(self):
        form_data = {
            "username": "user_name",
            "password1": "3134test",
            "password2": "3134test",
            "first_name": "first name",
            "last_name": "last name",
            "years_of_experience": "test"
        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_redactor_years_of_experience_is_negative(self):
        form_data = {
            "username": "user_name",
            "password1": "3134test",
            "password2": "3134test",
            "first_name": "first name",
            "last_name": "last name",
            "years_of_experience": -10,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class PrivateRedactorTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123",
            years_of_experience=3,
        )
        self.client.force_login(self.user)

    def test_create_redactor(self):
        form_data = {
            "username": "user_name",
            "password1": "3134test",
            "password2": "3134test",
            "first_name": "first name",
            "last_name": "last name",
            "years_of_experience": 3,
        }
        self.client.post(reverse("newspaper:redactor-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
