from django.db.models import fields
from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')

class StudentSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'


