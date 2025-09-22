from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.conf import settings

# Get the AUTH_USER_MODEL dynamically
AUTH_USER_MODEL = get_user_model()

class Detail(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    profileimage = models.ImageField(upload_to='images/', blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    companyname = models.CharField(max_length=100, blank=False, null=False)
    companylogo = models.ImageField(upload_to='images/', blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True, default="https://anitatai.in/")
    address = models.CharField(max_length=500, blank=True, null=False)

    # Gallery images
    gallery_image1 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)
    gallery_image6 = models.ImageField(upload_to='basic_gallery/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'Unnamed'} - {self.companyname or 'No Company'}"

class Detail_Primium(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    profileimage = models.ImageField(upload_to='images/', blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    phone_secondary = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=100, blank=True, null=True)
    companyname = models.CharField(max_length=100, blank=False, null=False)
    company_email = models.EmailField(blank=True, null=True)
    companylogo = models.ImageField(
        upload_to='images/', 
        blank=True, 
        null=True,
        default='none'
    )
    website = models.CharField(max_length=500, blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True, default="none")
    address = models.CharField(max_length=500, blank=False, null=False)
    location_url = models.CharField(max_length=100, blank=True, null=True)
    nature_of_business = models.CharField(max_length=200, blank=True, null=True)
    start_year = models.DateField(
        blank=True, 
        null=True,
        default=datetime.date(2000, 1, 1),
        validators=[
            MinValueValidator(datetime.date(1800, 1, 1)), 
            MaxValueValidator(datetime.date.today()) 
        ],
        help_text="Enter the date the company was started."
    )

    facebook_url = models.CharField(max_length=100, blank=True, null=True)
    twitter_url = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.CharField(max_length=100, blank=True, null=True)
    youtube_url = models.CharField(max_length=100, blank=True, null=True)
    pinterest_url = models.CharField(max_length=100, blank=True, null=True)
    linkedin_url = models.CharField(max_length=100, blank=True, null=True)
    telegram_url = models.CharField(max_length=100, blank=True, null=True)


    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    AGE_GROUP_CHOICES = [
        ('below_18', '<18'),
        ('18_40', '18-40'),
        ('above_40', '>40'),
    ]

    # Fields for Gender and Age Group
    speciality_1 = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        verbose_name="Gender"
    )

    speciality_2 = models.CharField(
        max_length=10,
        choices=AGE_GROUP_CHOICES,
        blank=True,
        null=True,
        verbose_name="Age Group"
    )
    speciality_3 = models.CharField(max_length=200, blank=True, null=True)

    # Gallery images
    gallery_imagePrimium1 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium2 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium3 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium4 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium5 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium6 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)
    gallery_imagePrimium7 = models.ImageField(upload_to='premium_gallery/', blank=True, null=True)  

    last_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'Unnamed'} - {self.companyname or 'No Company'}"