from django import forms
from .models import Profile, PortfolioItem

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'bio', 'profile_picture', 'country', 'city', 
                 'phone_number', 'website', 'social_media', 'skills', 'experience']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 4}),
            'social_media': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter social media links in JSON format'}),
        }

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['title', 'description', 'media_file', 'media_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        } 