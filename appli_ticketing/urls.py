"""Appli_Ticketing URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', main_views.dashboard, name='dashboard'),  # Added this line
    path('tickets/', include('tickets.urls')),
    # Auth URLs (main app only)
    path('accounts/login/', main_views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('accounts/register/', main_views.register, name='register'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]