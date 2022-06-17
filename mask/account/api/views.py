from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import Team_leaderSignupSerializer, Team_memberSignupSerializer, Userserializer 

class Team_leadersignupView(generics.GenericAPIView):
	serializer_class=Team_leaderSignupSerializer
	def post(self, request,*args, **kwargs):
		serializer=self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user=serializer.save()
		return response({
			"user":Userserializer(user,context=self.get_serializer_context()).data,
			"token":Token.objects.get(user=user).key,
			"massage":"account created sucessfully"


			})


class Team_membersignupView(generics.GenericAPIView):
	serializer_class=Team_memberSignupSerializer
	def post(self, request,*args, **kwargs):
		serializer=self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user=serializer.save()
		return response({
			"user":Userserializer(user, context=self.get_serializer_context()).data,
			"token":Token.objects.get(user=user).key,
			"massage":"account created sucessfully"


			})



