from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def save(self, **kwargs):

        new_user = User.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            password= self.validated_data['password'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )

        new_user.save()

        new_token = Token.objects.create(user=new_user)