# """
# Test models.
# """

# from django.test import TestCase
# from django.contrib.auth import get_user_model

# class ModelTests(TestCase):

#     def test_create_user_with_email(self):

#         email = "test@example.com"
#         password = "testpass123"
#         user = get_user_model().objects.create_user(
#             username=email,
#             email=email,
#             password=password
#         )

#         self.assertEqual(user.username, email)
#         self.assertEqual(user.email, email)
#         self.assertTrue(user.check_password(password))