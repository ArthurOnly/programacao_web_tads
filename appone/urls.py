from django.urls import path

import appone.views.questions as question_views
import appone.views.auth as auth_views

urlpatterns = [
    path('questions', question_views.index, name='questions_index'),
    path('questions/<int:id>', question_views.show, name='questions_show'),
    path('questions/<int:id>/vote', question_views.vote, name='questions_vote'),
    path('questions/<int:id>/vote/new', question_views.vote_post, name='questions_vote_post'),
    path('questions/<int:id>/result', question_views.result, name='questions_result'),
]