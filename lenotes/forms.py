from django import forms
from lenotes.models import Group, Diary, Invitation
from markdownx.fields import MarkdownxFormField

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'intro',
        ]
        labels = {
            'name': 'Group Name',
            'intro': 'Group Introduce',
        }

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = [
            'content',
        ]
        labels = {
            'content' : 'Content ( Markdown supportted )',
        }
    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['content'] = MarkdownxFormField()
        self.fields['content'].label = 'Content ( Markdown supportted )'

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['invite_id']
        labels = {'invite_id': 'Invite ID'}
    def get_id(self):
        return self.fields['invite_id'] 