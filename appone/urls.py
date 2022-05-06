from django.urls import path

import appone.views.home as home_views
import appone.views.auth as auth_views

urlpatterns = [
    path('', home_views.home, name='home'),
    path('auth/sign-in', auth_views.sign_in, name="sign-in")
]