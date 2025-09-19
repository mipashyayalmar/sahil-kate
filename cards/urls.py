from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    # Normal Card Routes
    path('generateForm/', views.generateForm, name='generateForm'),
    path('generate/<int:id>/', views.generate, name='generate'),
    path('closead/<int:id>/<int:theme>/', views.closead, name='closead'),
    path('form/', views.form, name='form'),
    path('download/<int:id>/<int:theme>/', views.download, name='download'),
    path('view/<int:id>/<int:theme>/', views.view, name='view'),
    path('edit/<int:id>/', views.edit_card, name='edit_card'),

    # Premium Card Routes
    path('download/premium/<int:id>/<int:theme>/', views.download_premium, name='download_premium'),

    path('premium-form/', views.premium_form, name='premium_form'),  # New premium card creation
    path('premium-form/<int:premium_id>/', views.premium_form, name='edit_premium_form'),  # Edit existing premium card
    path('premium/view/<int:id>/<int:theme>/', views.view_premium,  name='view_premium_card'),
    path('cardsgeneratepremium/<int:id>/', views.generatePremiumForm, name='generate_premium_form'),
]
