
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),    
    path('cards', include('cards.urls', namespace='cards')),
    path('user', include('user.urls', namespace='user')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('change_password',views.change_password,name='change_password'),
    path('accounts/', include('allauth.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('google/callback', views.google_callback, name='google_callback'),
]
