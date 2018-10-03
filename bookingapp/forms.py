from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


# admin.site.register(Post)

class myregistrationform(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def save(self,commit=True):
        user=super(myregistrationform,self).save(commit=False)
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'name','check_in','check_out','date','date_joined'}
