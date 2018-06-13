from django import forms
from markdownx.fields import MarkdownxFormField
from lenotes.models import Group, Diary, Invitation

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'intro',
            'profile',
        ]
        labels = {
            'name': 'Group Name',
            'intro': 'Group introduce',
        }

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = [
            'name',
            'content',
        ]
        labels = {
            'name' : 'Name',
            'content' : 'Content',
        }
    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['content'] = MarkdownxFormField()
        self.fields['content'].label = 'Content'

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['invite_id']
        labels = {'invite_id': 'Invite ID'}
    def get_id(self):
        return self.fields['invite_id']