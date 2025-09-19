from django import forms
from .models import Detail

class EditDetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = [
            'name', 'email', 'role', 'phone', 'profileimage', 'companyname',
            'companylogo', 'website', 'company_website', 'address',
            'gallery_image1', 'gallery_image2', 'gallery_image3',
            'gallery_image4', 'gallery_image5', 'gallery_image6'
        ]

   
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


from django import forms
from .models import Detail_Primium

class PremiumDetailForm(forms.ModelForm):
    class Meta:
        model = Detail_Primium
        fields = [
            'name', 'email', 'role', 'profileimage', 'phone', 'phone_secondary', 'whatsapp_no', 
            'companyname', 'company_email', 'companylogo', 'website', 'company_website', 'address', 
            'location_url', 'nature_of_business', 'speciality_1', 'speciality_2', 'speciality_3',
            'gallery_imagePrimium1', 'gallery_imagePrimium2', 'gallery_imagePrimium3', 
            'gallery_imagePrimium4', 'gallery_imagePrimium5', 'gallery_imagePrimium6','gallery_imagePrimium7',
            'last_message','start_year',
            # Include social media fields
            'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url', 
            'pinterest_url', 'linkedin_url', 'telegram_url'
        ]
        widgets = {
            'last_message': forms.Textarea(attrs={'rows': 4}),
        }
