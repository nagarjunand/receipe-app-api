from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """ Test creating a new user with an email is successfull"""
        email = 'naga@naga.com'
        password = 'Test@12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'naga@NAGA.COm'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            # This will fail if inside statement not raised value error
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@naga.com',
            'test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
