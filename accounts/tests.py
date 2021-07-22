from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()
class UserTestCase(TestCase):
    
    def setUp(self): # Case is important 
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('some_123_password')
        user_a.save()
        self.user_a = user_a


    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    # def test_user_password(self):
    #     self.assertTrue(self.user_a.check_password(self.user_a_pw))

    def test_user_password(self):
        user_a = User.objects.get(username="cfe")
        self.assertTrue(self.user_a.check_password(self.user_a_pw))


    def test_login_url(self):
        login_url = settings.LOGIN_URL
        #response = self.client.post(url, {}, follow=True)
        data = {"username": "cfe", "password": self.user_a_pw}
        response = self.client.post(login_url, data, follow=True) 
        print(dir(response))
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        #self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)