from rest_framework import generics, status
from rest_framework.response import Response
from .models import Instructor, Dancer, DanceStudio, Subscription, User, UserProfile
from .serializers import InstructorSerializer, UserProfileSerializer, DancerSerializer, DanceStudioSerializer, SubscriptionSerializer
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta


class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        # Extract data from the request
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        # Add more fields as needed for user registration

        # Validate input data
        if not username or not email or not password:
            return Response({'error': 'Username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new User instance
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        # Create a new UserProfile associated with the User
        user_profile_data = {
            'user': new_user.id,
            # Add more fields as needed for the user profile
        }
        serializer = UserProfileSerializer(data=user_profile_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registration successful'}, status=status.HTTP_201_CREATED)
        else:
            # If there's an issue creating the UserProfile, delete the User instance
            new_user.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class DancerListCreateView(generics.ListCreateAPIView):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer

class DanceStudioListCreateView(generics.ListCreateAPIView):
    queryset = DanceStudio.objects.all()
    serializer_class = DanceStudioSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        # Extract data from the request
        dancer_id = request.data.get('dancer')
        studio_id = request.data.get('studio')
        is_premium = request.data.get('is_premium', False)

        # Check if the dancer and studio are valid users
        try:
            dancer = User.objects.get(id=dancer_id)
            studio = User.objects.get(id=studio_id)
        except User.DoesNotExist:
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate other input data as needed

        # Calculate end_date based on the subscription type
        if is_premium:
            # Premium subscription is for one month
            end_date = calculate_end_date_one_month()
        else:
            # Basic subscription is for one session
            end_date = calculate_end_date_one_session()

        # Create the subscription
        subscription_data = {
            'dancer': dancer,
            'studio': studio,
            'is_premium': is_premium,
            'start_date': timezone.now().date(),
            'end_date': end_date,
        }

        serializer = SubscriptionSerializer(data=subscription_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Subscription created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def calculate_end_date_one_month():
    return timezone.now().date() + timedelta(days=30)

def calculate_end_date_one_session():
    return timezone.now().date() + timedelta(days=1)

def HomeView(request):
    return HttpResponse("Welcome to Dance Flow!")