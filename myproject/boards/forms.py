from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': "What's on your mind?"}
        ),
        max_length=4000,
        help_text='4000 character maximum.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']