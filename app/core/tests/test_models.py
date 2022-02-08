from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def create_user_with_email_successful(self):
        """Test creating a user with email successful"""
        email = 'abc@gmail.com'
        password = 'abcd1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def tets_new_user_email_normalized(self):
        ''' Test the email from new user is normalized '''
        email = 'ABC@gmail.COM'
        user = get_user_model().objects.create_user(email, 'abcd1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' Test creating new user with no email raises error '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abcd1234')

    def test_create_new_superuser(self):
        '''Test creating a new superuser '''
        user = get_user_model().objects.create_superuser(
            'abc@gmail.com',
            'abcd1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


