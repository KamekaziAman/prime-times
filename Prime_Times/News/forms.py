from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full text-4xl font-bold bg-transparent border-none focus:ring-0 focus:outline-none placeholder-gray-500',
                'placeholder': 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full text-lg bg-transparent border-none focus:ring-0 focus:outline-none placeholder-gray-500 resize-none',
                'rows': 15,
                'placeholder': 'Write an article or news description…'
            }),
            'image': forms.ClearableFileInput(attrs={
            'class': 'block text-sm text-gray-300 cursor-pointer'
            }),
        }
