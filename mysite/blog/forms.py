from django import forms
from blog.models import Post,Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields = ('username','password','first_name','last_name','email')


class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text','docfile',)
        widgets={
         'title':forms.TextInput(attrs={'class':'textinputclass'}),
         #'text':forms.CharField(widget=forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}))
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
        widgets={
         'author':forms.TextInput(attrs={'class':'textinputclass'}),
        # 'text':forms.CharField(widget=forms.Textarea(attrs={'class':'editable medium-editor-textarea '}))
        }
#class DocumentForm(forms.Form):
#    docfile = forms.FileField(
#        label='Select a file',
#    )
