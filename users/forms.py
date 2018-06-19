from django import forms
#from markdown import MarkdownFormField
from users.models import UserInfo, Message


#class ProfileForm(forms.Form):
 #   upProfile = forms.FileField()

class InfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'name',
            'gender',
            'email',
            'intro',
        
        ]
        labels = {
            'name': 'User Name',
            'gender': 'Gender',
            'email': 'Email',
            'intro': 'User introduce',
        }

class MsgForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'receiver',
            'text',
        ]
        labels = {
            'receiver' : 'Receiver',
            'text': ''
        }
