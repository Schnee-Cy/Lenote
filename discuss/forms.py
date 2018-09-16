from django import forms
from discuss.models import Topic, Discuss
from markdownx.fields import MarkdownxFormField

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'name',
            'content',
        ]
        labels = {
            'name' : 'Topic',
            'content' : 'Content ( Markdown supportted )',
        }
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['content'] = MarkdownxFormField()
        self.fields['content'].label = 'Content ( Markdown supportted )'

class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = [ 
            'content', 
            'mention',
         ]
        
    def __init__(self, *args, **kwargs):
        super(DiscussForm, self).__init__(*args, **kwargs)
        self.fields['content'] = MarkdownxFormField()
        self.fields['mention'].label = 'Mention someone: '
        self.fields['mention'].initial = 'Example: "username1, username2"'