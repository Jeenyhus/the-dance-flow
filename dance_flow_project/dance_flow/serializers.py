from rest_framework import serializers
from .models import Instructor, Dancer, DanceStudio, Subscription, User, UserProfile

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class DancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dancer
        fields = '__all__'

class DanceStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceStudio
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'