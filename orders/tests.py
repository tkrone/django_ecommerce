from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()
class OrderTestCase(TestCase):
    def setUp(self):
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('some_123_password')
        user_a.save()
        self.user_a = user_a
    
    # def test_create_order(self):
    #     obj = Order.objects.create(user=self.user_as, product=product_a)