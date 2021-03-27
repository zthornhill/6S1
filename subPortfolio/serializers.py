from rest_framework import serializers
from .models import User, Subscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'phoneNum', 'address', 'city', 'state', 'zipcode')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('pk', 'user', 'acctNum', 'sub_Name', 'sub_Description', 'sub_Price', 'acquired_date', 'end_date')
