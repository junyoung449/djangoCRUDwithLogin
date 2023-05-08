from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'row':7,
                'col':50
            }
        )
    )
    
    
    class Meta:
        model = Article
        fields = ("title", "content", "image",)
