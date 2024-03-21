from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
def add(a,b):
    return a+b

class UserTest(TestCase):

    def test_add(self):#test_  is compulsory           # assert is simplify testCase pass or fail
        self.assertEqual(add(5,5),10)

    def setUp(self):
       self.user=User.objects.create(username="TestUser",
                            first_name="TestFname",
                            last_name="TestLastname",
                            email="TestUser@123gmail.com",
                            password="User@123")
       
    def test_create_user(self):
      user=User.objects.get(username="TestUser")
      self.assertEqual(user.username,self.user.username)

    def test_update_user(self):
      user=User.objects.get(username="TestUser")
      oldEmail=user.email
      user.email="updatedemail@gmail.com"
      user.save()

      user=User.objects.get(username="TestUser")
      self.assertNotEqual(oldEmail,user.email)