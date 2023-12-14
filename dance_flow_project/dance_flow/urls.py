# dance_flow/urls.py
from django.urls import path
from .views import InstructorListCreateView, UserProfileCreateView, SubscriptionCreateView, DancerListCreateView, DanceStudioListCreateView, SubscriptionListCreateView, HomeView

urlpatterns = [
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('dancers/', DancerListCreateView.as_view(), name='dancer-list-create'),
    path('dance_studios/', DanceStudioListCreateView.as_view(), name='dance-studio-list-create'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('user-profiles/create/', UserProfileCreateView.as_view(), name='user-profile-create'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('', HomeView, name='home'),
]
