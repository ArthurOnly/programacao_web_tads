from django.urls import path

import appone.views.questions as question_views
import appone.views.auth as auth_views

urlpatterns = [
    path('questions', question_views.index, name='questions_index'),
    path('questions/<int:id>', question_views.show, name='questions_show'),
]