from .models import User,UserManager
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email','profile','is_staff','is_active','date_joined')
        