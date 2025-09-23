from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import google_auth_oauthlib
from cards.models import Detail, Detail_Primium
from user.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from django.contrib.auth import login

def home(request):
    if request.session.get('username'):
        cards = Detail.objects.filter(created_for=User.objects.get(username=request.session['username']))
        return render(request,'home/index.html',{
            'cards':cards
        } )
    return render(request, 'home/index.html')

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

@login_required(login_url="user:signin")
def profile(request):
    user = request.user
    
    # If user is superuser or admin, show all profiles
    if user.is_superuser or user.is_staff:
        all_users = User.objects.all()
        
        # Precompute card counts for each user
        users_with_counts = []
        for user_obj in all_users:
            regular_card_count = Detail.objects.filter(created_for=user_obj).count()
            premium_card_count = Detail_Primium.objects.filter(created_for=user_obj).count()
            
            users_with_counts.append({
                'user': user_obj,
                'regular_card_count': regular_card_count,
                'premium_card_count': premium_card_count
            })
        
        # Calculate totals for stats
        total_regular_cards = sum(user_data['regular_card_count'] for user_data in users_with_counts)
        total_premium_cards = sum(user_data['premium_card_count'] for user_data in users_with_counts)
        
        context = {
            "user": user, 
            'users_with_counts': users_with_counts,
            'total_regular_cards': total_regular_cards,
            'total_premium_cards': total_premium_cards,
            'new_users_today': User.objects.filter(date_joined__date=timezone.now().date()).count(),
            'is_admin': True
        }
        return render(request, "home/profile.html", context)
    
    # Regular user sees only their own data
    cards = Detail.objects.filter(created_for=user)
    cards_detail = Detail_Primium.objects.filter(created_for=user)
    
    context = {
        "user": user, 
        'cards': cards, 
        'cards_detail': cards_detail,
        'is_admin': False
    }
    return render(request, "home/profile.html", context)

@login_required(login_url="user:signin")
def admin_user_profile(request, user_id):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('profile')
    
    user_profile = get_object_or_404(User, id=user_id)
    
    # Get the user's cards - use created_for instead of user
    cards = Detail.objects.filter(created_for=user_profile)
    cards_detail = Detail_Primium.objects.filter(created_for=user_profile)
    
    context = {
        'user_profile': user_profile,
        'cards': cards,
        'cards_detail': cards_detail,
        'is_admin_viewing': True,
        'user': request.user,  # Current admin user
    }
    return render(request, 'home/admin_user_profile.html', context)

@login_required(login_url="user:signin")
def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.phone = request.POST.get("phone")
        user.username = request.POST.get("username")
        user.save()
        return render(request, "home/profile.html", {"user": user, "message": "Profile Updated Successfully"})
    return render(request, "home/edit_profile.html", {"user": user})
        
@login_required(login_url="user:signin")
def change_password(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        print(user.password)
        if check_password(request.POST.get("password"), user.password):
            if request.POST.get("new_password") == request.POST.get("repeat_password"):
                user.set_password(request.POST.get("new_password"))
                user.save()
                return render(request, "home/profile.html", {"user": user, "message": "Password Changed Successfully"})
            else:
                return render(request, "home/change_password.html", {"user": user, "message": "Passwords did not match"})
        else:
            return render(request, "home/change_password.html", {"user": user, "message": "Old Password did not match"})
    return render(request, "home/change_password.html", {"user": user})

def google_callback(request):
    # Exchange the authorization code for a token
    print('shdgf')
    token = google_auth_oauthlib.fetch_token(authorization_response=request.get_full_path())
    
    # Get user information from Google API
    google_api = build('oauth2', 'v2', credentials=token)
    user_info = google_api.userinfo().get().execute()
    
    # Create or retrieve the User object
    user, _ = User.objects.get_or_create(username=user_info['email'])
    request.session['username'] = user.username
    request.session['oauth'] = True
    # Log in the user
    login(request, user)
    return redirect('/')