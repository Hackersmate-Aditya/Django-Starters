from django.urls import path


from . import views

urlpatterns = [                                                                       #all paths here
    path('choices', views.ChoiceView.as_view()),
    path('questions', views.QuestionView.as_view()),
    path('questions/<int:id>', views.QuestionByPK.as_view()),
    path('choices/<int:id>', views.ChoiceByFK.as_view()),
    path('votes/<int:id>', views.votes.as_view())
]
