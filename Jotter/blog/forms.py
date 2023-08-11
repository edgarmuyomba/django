from django import forms
from .models import Post, Comment, Topic

class PostForm(forms.ModelForm):
    error_css_class = "error"
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'post-title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'post-text', 'placeholder': 'Text'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'tags', 'form': 'newPostForm'}))
    topic = forms.ModelChoiceField(empty_label='Select a topic', queryset=Topic.objects.all(), widget=forms.Select(attrs={'form': 'newPostForm'}))
    class Meta:
        model = Post 
        fields = ['title', 'text', 'topic', 'tags']
    field_order = ['title', 'text', 'topic', 'tags']

    def clean(self):
        super(PostForm, self).clean()
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        tags = self.cleaned_data['tags']
        topic = self.cleaned_data['topic']

        if len(title) < 10:
            self.add_error('title', 'Please enter a more descriptive title')

        if len(text) < 200:
            self.add_error('text', 'Minimum text length is 200 characters')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']