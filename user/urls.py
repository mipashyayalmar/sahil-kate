from django.urls import path,include
from .import views

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
app_name = 'user'
urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('logout', views.logout_view,name='logout_view'),
     path('verify_email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
    #  path('password-reset/', PasswordResetView.as_view(template_name='user/password_reset.html'),name='password-reset'),
      path('password-reset/', views.CustomPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    
]
