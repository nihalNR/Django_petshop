from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        labels={"username":"Enter Username"}
        #fields="__all__"