from django.urls import path
from .views import Team_leadersignupView, Team_membersignupView


urlpatterns=[
      path('signup/team_leader/',Team_leadersignupView.as_view()),
      path('signup/team_member/',Team_membersignupView.as_view())
]
