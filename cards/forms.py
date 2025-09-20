from django import forms
from django.core.files.uploadedfile import UploadedFile
from .models import Detail, Detail_Primium

class EditDetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = [
            'name', 'email', 'role', 'phone', 'profileimage', 'companyname',
            'companylogo', 'website', 'company_website', 'address',
            'gallery_image1', 'gallery_image2', 'gallery_image3',
            'gallery_image4', 'gallery_image5', 'gallery_image6'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your role'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'companyname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your website URL'}),
            'company_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company website URL'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validate optional URL fields
        url_fields = ['website', 'company_website']
        for field in url_fields:
            url = cleaned_data.get(field)
            if url and not url.startswith(('http://', 'https://')):
                self.add_error(field, 'Enter a valid URL starting with http:// or https://.')

        # Validate optional file fields
        file_fields = ['profileimage', 'companylogo', 'gallery_image1', 'gallery_image2',
                       'gallery_image3', 'gallery_image4', 'gallery_image5', 'gallery_image6']
        for field in file_fields:
            file = cleaned_data.get(field)
            if isinstance(file, UploadedFile) and file.size > 5 * 1024 * 1024:  # 5MB limit
                self.add_error(field, 'File size must be under 5MB.')

        return cleaned_data

class PremiumDetailForm(forms.ModelForm):
    class Meta:
        model = Detail_Primium
        fields = [
            'name', 'email', 'role', 'profileimage', 'phone', 'phone_secondary', 'whatsapp_no',
            'companyname', 'company_email', 'companylogo', 'website', 'company_website', 'address',
            'location_url', 'nature_of_business', 'speciality_1', 'speciality_2', 'speciality_3',
            'gallery_imagePrimium1', 'gallery_imagePrimium2', 'gallery_imagePrimium3',
            'gallery_imagePrimium4', 'gallery_imagePrimium5', 'gallery_imagePrimium6', 'gallery_imagePrimium7',
            'last_message', 'start_year',
            'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url',
            'pinterest_url', 'linkedin_url', 'telegram_url'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your role'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'phone_secondary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your secondary phone number'}),
            'whatsapp_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your WhatsApp number'}),
            'companyname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company name'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company email'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your website URL'}),
            'company_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company website URL'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'location_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location URL'}),
            'nature_of_business': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nature of business'}),
            'speciality_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first specialty'}),
            'speciality_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your second specialty'}),
            'speciality_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your third specialty'}),
            'last_message': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter your message here'}),
            'start_year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Facebook URL'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Twitter URL'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Instagram URL'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your YouTube URL'}),
            'pinterest_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Pinterest URL'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your LinkedIn URL'}),
            'telegram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Telegram URL'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validate optional URL fields
        url_fields = ['website', 'company_website', 'location_url', 'facebook_url', 'twitter_url',
                      'instagram_url', 'youtube_url', 'pinterest_url', 'linkedin_url', 'telegram_url']
        for field in url_fields:
            url = cleaned_data.get(field)
            if url and not url.startswith(('http://', 'https://')):
                self.add_error(field, 'Enter a valid URL starting with http:// or https://.')

        # Validate optional file fields
        file_fields = ['profileimage', 'companylogo', 'gallery_imagePrimium1', 'gallery_imagePrimium2',
                       'gallery_imagePrimium3', 'gallery_imagePrimium4', 'gallery_imagePrimium5',
                       'gallery_imagePrimium6', 'gallery_imagePrimium7']
        for field in file_fields:
            file = cleaned_data.get(field)
            if isinstance(file, UploadedFile) and file.size > 5 * 1024 * 1024:  # 5MB limit
                self.add_error(field, 'File size must be under 5MB.')

        return cleaned_data