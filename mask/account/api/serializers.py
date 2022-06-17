from rest_framework import serializers
from account.models import User, Team_task, Team_model

class Userserializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','email','is_team_leader'],

class Team_leaderSignupSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
	class Meta:
		model=User
		fields=['username','password','password2']
		exta_kwargs={
		'password':{'write_only':True}
		}

		def save(self, **kwargs):
			user=User(
				username=self.validated_data['username'],
				email=self.validated_data['email']

				)
			password=self.validated_data['password']
			password2=self.validated_data['password2']
			if password !=password2:
				raise serializers.validationError({"error":"password does not match"})
			user.set_password(password)
			user.is_team_leader=True
			user.save()
			Team_leader.objects.create(user=user)

			return user




class Team_memberSignupSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
	class Meta:
		model=User
		fields=['username','password','password2']
		exta_kwargs={
		'password':{'write_only':True}
		}

		def save(self, **kwargs):
			user=User(
				username=self.validated_data['username'],
				email=self.validated_data['email']

				)
			password=self.validated_data['password']
			password2=self.validated_data['password2']
			if password != password2:
				raise serializers.validationError({"error":"password does not match"})
			user.set_password(password)
			user.is_team_member=True
			user.save()
			Team_member.objects.create(user=user)

			return user



