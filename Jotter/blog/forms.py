from django import forms
from .models import Post, Comment, Topic

def titleValidation(value):
    if len(value) < 10:
        raise forms.ValidationError("Please enter a more descriptive title")

def textValidation(value):
    if len(value) < 200:
        raise forms.ValidationError("Minimum post length is 200 characters")

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'post-title'}), validators=[titleValidation])
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'post-text', 'placeholder': 'Text'}), validators=[textValidation])
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'tags'}))
    topic = forms.ModelChoiceField(empty_label='Select a topic', queryset=Topic.objects.all())
    class Meta:
        model = Post 
        fields = []
    field_order = ['title', 'text', 'topic', 'tags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']