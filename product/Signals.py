from django.contrib.auth.signals import *
#user_logged_in , user_logged_out
from django.contrib.auth.models import User

from django.dispatch import receiver

from django.db.models.signals import *
from .models import product

@receiver(user_logged_in,sender=User)
def log_In(sender,request,user,**kwargs):
    print("***")
    print("Logged In Successfully")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguments:",kwargs)
    print("******")

@receiver(user_logged_out,sender=User)
def log_Out(sender,request,user,**kwargs):
    print("***")
    print("Logged Out Successfully")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguments:",kwargs)
    print("******")

@receiver(post_save,sender=product)
def ProductCreateSignal(sender,instance,**kwargs):
        print("******Product Created******")
        print("**********")
        print("sender:",sender)
        print("Instance:",instance)
        print("arguments:",kwargs)
        print("********")

@receiver(post_delete,sender=product)
def ProductCreateSignal(sender,instance,**kwargs):
        print("******Product Deleted******")
        print("**********")
        print("sender:",sender)
        print("Instance:",instance)
        print("arguments:",kwargs)
        print("********")