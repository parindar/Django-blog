from django import forms
from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(forms.ModelForm):
	post_id = forms.IntegerField(widget=forms.HiddenInput())

	class Meta:
	    model = Comment
	    fields = ('name', 'desc',)	    
	    widgets = {
            'desc': Textarea(attrs={'cols': 85, 'rows': 3}),
        }
        