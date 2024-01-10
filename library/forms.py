from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30,label="姓名")
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}),label="回饋意見")


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']
        labels = {
            'enrollment': '使用者名稱',
            'branch': '使用者序號',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']
        labels = {
            'name':'書名',
            'author':'作者',
            'category': '種類'
        }
class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="姓名 和 isbn", to_field_name="isbn",label='姓名 和 isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="姓名 和 使用者名稱",to_field_name='enrollment',label='姓名和使用者名稱')

