from django.contrib.auth import get_user_model
from django.test import TestCase


# 'Code without tests is broken as designed.' JKM.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testUser',
            email='testUser@testemail.com',
            password='testPass'
        )

        self.assertEqual(user.username, 'testUser')
        self.assertEqual(user.email, 'testUser@testemail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='administrator',
            email='administrator@email.com',
            password='admin-pass'
        )

        self.assertEqual(admin_user.username, 'administrator')
        self.assertEqual(admin_user.email, 'administrator@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
