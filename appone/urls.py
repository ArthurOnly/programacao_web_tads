from django.urls import path

import appone.views.users as users_views

urlpatterns = [
    path('/users', users_views.index, name='index'),
]