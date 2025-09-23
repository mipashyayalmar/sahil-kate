from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from cards.models import Detail
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from CardGenerator import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'user/signin.html', {'message': 'User already exists with that username. Please sign in.'})
        
        # Create the new user - no email verification needed
        user = User.objects.create_user(username=username, password=password)
        user.is_active = True  # Activate immediately
        user.save()
        
        # Automatically log in the user after signup
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            request.session['username'] = username
            request.session.save()
            login(request, authenticated_user)
            return redirect('cards:premium_form')  # Redirect to homepage after successful signup and login
        
        return render(request, 'user/signup.html', {'message': 'Account created but failed to log in automatically. Please sign in.'})
    
    return render(request, 'user/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists
        if not User.objects.filter(username=username).exists():
            return render(request, 'user/signup.html', {'message': "User doesn't exist. Please sign up"})
        
        # Authenticate the user with credentials
        authenticated_user = authenticate(username=username, password=password)
        
        if authenticated_user is not None:
            if authenticated_user.is_active:
                request.session['username'] = username
                request.session.save()
                login(request, authenticated_user)
                return redirect('/')
        
        return render(request, 'user/signin.html', {'message': 'Incorrect username or password'})
    
    return render(request, 'user/signin.html')


def logout_view(request):
    try:
        # Try to delete the 'username' from the session
        del request.session['username']
    except KeyError:
        # Handle the case where 'username' is not in the session
        pass
    
    # Save the session changes and log out the user
    request.session.save()
    logout(request)
    
    # Optionally redirect to home or another page after logout
    return render(request, 'user/signin.html', {'message': 'Logged out successfully'})


from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

class CustomPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'
    success_url = reverse_lazy('user:password_reset_done')  # Update the URL name
    email_template_name = 'user/reset_password.html'
    extra_email_context = {'protocol': 'http', 'domain':'businesscardgenerator-production.up.railway.app'}
    
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse_lazy

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')
    form_class = SetPasswordForm