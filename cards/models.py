from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.conf import settings 
# Get the AUTH_USER_MODEL dynamically
AUTH_USER_MODEL = get_user_model()

class Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    profileimage = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    companylogo = models.ImageField(upload_to='images/')
    website = models.CharField(max_length=500)
    company_website = models.CharField(max_length=100, default="https://websenz.in/")
    address = models.CharField(max_length=500)

    # Gallery images
    gallery_image1 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)
    gallery_image2 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)
    gallery_image3 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)
    gallery_image4 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)
    gallery_image5 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)
    gallery_image6 = models.ImageField(upload_to='basic_gallery/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.companyname}"


class Detail_Primium(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    profileimage = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=100)
    phone_secondary = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=100, blank=True, null=True)
    companyname = models.CharField(max_length=100)
    company_email = models.EmailField(blank=True, null=True)
    companylogo = models.ImageField(
        upload_to='images/', 
        default='https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg'
    )
    website = models.CharField(max_length=500)
    company_website = models.CharField(max_length=100, default="https://websenz.in/")
    address = models.CharField(max_length=500)
    location_url = models.URLField(blank=True, null=True)
    nature_of_business = models.CharField(max_length=200, blank=True, null=True)
    start_year = models.DateField(
        default=datetime.date(2000, 1, 1),  
        validators=[
            MinValueValidator(datetime.date(1800, 1, 1)), 
            MaxValueValidator(datetime.date.today()) 
        ],
        help_text="Enter the date the company was started."
    )

    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)

    # Specialities
    speciality_1 = models.CharField(max_length=200, blank=True, null=True)
    speciality_2 = models.CharField(max_length=200, blank=True, null=True)
    speciality_3 = models.CharField(max_length=200, blank=True, null=True)

    # Gallery images
    gallery_imagePrimium1 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium2 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium3 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium4 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium5 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium6 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)
    gallery_imagePrimium7 = models.ImageField(upload_to='premium_gallery/', null=True, blank=True)  


    last_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.companyname}"

