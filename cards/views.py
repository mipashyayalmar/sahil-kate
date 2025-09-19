from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Detail, Detail_Primium
from .forms import EditDetailForm, PremiumDetailForm

User = get_user_model()

def my_premium_cards(request):
    if not request.user.is_authenticated:
        return redirect('user:signin')
    cards_detail = Detail_Primium.objects.filter(created_for=request.user)
    return render(request, 'cards/card2.html', {'cards_detail': cards_detail})



from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Detail_Primium
from .forms import PremiumDetailForm
import datetime

def generatePremiumForm(request, id):
    # Fetch the existing Detail_Primium object
    premium_detail = get_object_or_404(Detail_Primium, id=id)

    if request.method == 'POST':
        # Bind the form with POST data and FILES, and associate it with the instance
        form = PremiumDetailForm(request.POST, request.FILES, instance=premium_detail)
        if form.is_valid():
            # Extracting additional fields manually
            premium_detail.name = request.POST['name']
            premium_detail.email = request.POST['email']
            premium_detail.role = request.POST['role']
            premium_detail.phone = request.POST['phone']
            premium_detail.phone_secondary = request.POST.get('phone_secondary', None)
            premium_detail.whatsapp_no = request.POST.get('whatsapp_no', None)
            premium_detail.companyname = request.POST['companyname']
            premium_detail.company_email = request.POST.get('company_email', None)
            premium_detail.companylogo = request.FILES.get('companylogo', None)
            premium_detail.website = request.POST['website']
            premium_detail.company_website = request.POST['company_website']
            premium_detail.address = request.POST['address']
            premium_detail.location_url = request.POST.get('location_url', None)
            premium_detail.nature_of_business = request.POST.get('nature_of_business', None)
            premium_detail.speciality_1 = request.POST.get('speciality_1', None)
            premium_detail.speciality_2 = request.POST.get('speciality_2', None)
            premium_detail.speciality_3 = request.POST.get('speciality_3', None)
            premium_detail.gallery_imagePrimium1 = request.FILES.get('gallery_imagePrimium1', None)
            premium_detail.gallery_imagePrimium2 = request.FILES.get('gallery_imagePrimium2', None)
            premium_detail.gallery_imagePrimium3 = request.FILES.get('gallery_imagePrimium3', None)
            premium_detail.gallery_imagePrimium4 = request.FILES.get('gallery_imagePrimium4', None)
            premium_detail.gallery_imagePrimium5 = request.FILES.get('gallery_imagePrimium5', None)
            premium_detail.gallery_imagePrimium6 = request.FILES.get('gallery_imagePrimium6', None)
            premium_detail.gallery_imagePrimium7 = request.FILES.get('gallery_imagePrimium7', None)
            premium_detail.last_message = request.POST.get('last_message', None)
            
            start_year_str = request.POST.get('start_year', None)
            if start_year_str:
                try:
                    premium_detail.start_year = datetime.datetime.strptime(start_year_str, "%Y-%m-%d").date()
                except ValueError:
                    messages.error(request, 'Invalid date format for the start year.')
                    return render(request, 'cards/premiumgenerate.html', {'form': form, 'premium_detail': premium_detail})
            
            # Adding social media fields
            premium_detail.facebook_url = request.POST.get('facebook_url', None)
            premium_detail.twitter_url = request.POST.get('twitter_url', None)
            premium_detail.instagram_url = request.POST.get('instagram_url', None)
            premium_detail.youtube_url = request.POST.get('youtube_url', None)
            premium_detail.pinterest_url = request.POST.get('pinterest_url', None)
            premium_detail.linkedin_url = request.POST.get('linkedin_url', None)
            premium_detail.telegram_url = request.POST.get('telegram_url', None)

            # Save the updated premium_detail instance
            premium_detail.save()
            messages.success(request, 'Premium Card updated successfully')
            return redirect('cards:my_premium_cards', {
                'message': "Card Generated Successfully", 
                'premium_detail': premium_detail, 
                'username': premium_detail.name, 
                'id': premium_detail.id
            })
        else:
            # Display form errors if any
            messages.error(request, 'There was an error updating the Premium Card. Please check the form for errors.')
    else:
        # Display the form with the existing instance data
        form = PremiumDetailForm(instance=premium_detail)

    # Render the form with the premium_detail context
    return render(request, 'cards/premiumgenerate.html', {'form': form, 'premium_detail': premium_detail})

  
      
def generateForm(request):
    if request.session.get('username') and request.method == 'POST':
        name = request.POST['name']
        profileimage = request.FILES['profileimage']
        email = request.POST['email']
        role = request.POST['role']
        phone = request.POST['phone']
        companyname = request.POST['companyname']
        companylogo = request.FILES['logo']
        website = request.POST['website']
        company_website = request.POST['company_website']
        address = request.POST['address']
        gallery_image1 = request.FILES.get('gallery_image1', None)
        gallery_image2 = request.FILES.get('gallery_image2', None)
        gallery_image3 = request.FILES.get('gallery_image3', None)
        gallery_image4 = request.FILES.get('gallery_image4', None)
        gallery_image5 = request.FILES.get('gallery_image5', None)
        gallery_image6 = request.FILES.get('gallery_image6', None)
        created_for = User.objects.get(username=request.session['username'])
        details = Detail(
            name=name,
            email=email,
            role=role,
            phone=phone,
            profileimage=profileimage,
            companyname=companyname,
            companylogo=companylogo,
            website=website,
            company_website=company_website,
            address=address,
            gallery_image1=gallery_image1,
            gallery_image2=gallery_image2,
            gallery_image3=gallery_image3,
            gallery_image4=gallery_image4,
            gallery_image5=gallery_image5,
            gallery_image6=gallery_image6,
            created_for=created_for
        )
        details.save()
        messages.success(request, 'Card Generated Successfully')
        return render(request, 'cards/generate.html', {'message': "Card Generated Successfully", 'details': details, 'username': name, 'id': details.id})
    return render(request, 'user/signin.html', {'message': "You need to sign in to generate Cards"})

def edit_card(request, id):
    detail = get_object_or_404(Detail, id=id)
    if detail.created_for.username != request.session.get('username'):
        messages.error(request, 'You are not authorized to edit this card.')
        return redirect('home')
    if request.method == 'POST':
        form = EditDetailForm(request.POST, request.FILES, instance=detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card updated successfully.')
            return redirect('view_card', id=detail.id)
        messages.error(request, 'There was an error updating the card.')
    else:
        form = EditDetailForm(instance=detail)
    gallery_images = [detail.gallery_image1, detail.gallery_image2, detail.gallery_image3, detail.gallery_image4, detail.gallery_image5, detail.gallery_image6]
    return render(request, 'cards/edit_card.html', {'form': form, 'detail': detail, 'gallery_images': gallery_images})

def generate(request, id):
    if request.session.get('username') and request.method == 'GET':
        details = get_object_or_404(Detail, id=id)
        messages.success(request, 'Card Generated Successfully')
        return render(request, 'cards/generate.html', {'message': "Card Generated Successfully", 'details': details, 'username': details.name, 'id': details.id})
    return render(request, 'user/signin.html', {"message": "You need to sign in to generate Cards"})

def form(req):
    if req.session.get('username') is None:
        return render(req, 'user/signin.html', {'message': "You need to sign in to generate Cards"})
    return render(req, 'cards/form.html')
from django.shortcuts import render, redirect, get_object_or_404


def premium_form(request, premium_id=None):
    # Check if a premium_id is provided to edit an existing premium card
    if premium_id:
        premium_detail = get_object_or_404(Detail_Primium, id=premium_id)
        form = PremiumDetailForm(request.POST or None, request.FILES or None, instance=premium_detail)
    else:
        premium_detail = None
        form = PremiumDetailForm(request.POST or None, request.FILES or None)

    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to create or update a premium card.")
        return redirect('user:signin')

    
    if request.method == 'POST':
        if form.is_valid():
            premium_card = form.save(commit=False)  
            premium_card.created_for = request.user  
            try:
                premium_card.save()  
                messages.success(request, 'Premium card created/updated successfully!')

                
                return redirect('cards:generate_premium_form', id=premium_card.id)  
            except Exception as e:
                messages.error(request, f"An error occurred while saving the premium card: {str(e)}")
        else:
           
            messages.error(request, "Please correct the errors below.")

    
    context = {
        'form': form,
        'premium_detail': premium_detail
    }
    return render(request, 'cards/premium_form.html', context)




def view(req, id, theme):
    """
    View function to render normal cards.
    """
    details = get_object_or_404(Detail, id=id)
    template_name = 'cards/card' + str(theme) + '.html'
    
    return render(req, template_name, {
        'details': details,
        'id': id,
        'theme': theme
    })

def view_premium(req, id, theme):
    """
    View function to render premium cards.
    """
    details = get_object_or_404(Detail_Primium, id=id)
    template_name = 'cards/premium_card' + str(theme) + '.html'
    
    return render(req, template_name, {
        'premium_detail': details,
        'id': id,
        'theme': theme
    })


@login_required
def view_premium_card(req, id, theme):
    premium_detail = get_object_or_404(Detail_Primium, id=id)
    return render(req, 'cards/premium_card{}.html'.format(theme), {
        'premium_detail': premium_detail,
        'id': id,
        'theme': theme,
        'alert': "This is a premium card. Please sign in to access premium features."
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def download_premium(req, id, theme):
    premium_detail = get_object_or_404(Detail_Primium, id=id)
    
    user = User.objects.get(username=req.user.username)
    
    if user.paid_member:
        return redirect('payment:process_payment')
    
    
    if req.headers.get('X-Requested-With') == 'XMLHttpRequest':
        image_url = premium_detail.image.url if hasattr(premium_detail, 'image') and premium_detail.image else None
        
        if image_url:
            return JsonResponse({'image_url': image_url})
        else:
            return JsonResponse({'error': 'Image URL not found'}, status=404)

    return render(req, f'cards/premium_card{theme}.html', {
        'premium_detail': premium_detail,
        'id': id,
        'theme': theme,
        'paidmember': user.paid_member
    })


def download(req, id, theme):
    details = get_object_or_404(Detail, id=id)
    if 'username' in req.session:
        user = User.objects.get(username=req.session['username'])
        if not user.paid_member:
            return redirect('payment:process_payment')
        return render(req, 'cards/card' + str(theme) + '.html', {'details': details, 'id': id, 'theme': theme, "paidmember": user.paid_member})
    return render(req, 'cards/card' + str(theme) + '.html', {'details': details, 'id': id, 'theme': theme, "alert": "You need to sign in to download the card"})

def closead(req, id, theme):
    details = get_object_or_404(Detail, id=id)
    if 'username' in req.session:
        user = User.objects.get(username=req.session['username'])
        if not user.paid_member:
            return redirect('payment:process_payment')
        return render(req, 'cards/card' + str(theme) + '.html', {'details': details, 'id': id, 'theme': theme, "paidmember": user.paid_member})
    return redirect('user:signin')
