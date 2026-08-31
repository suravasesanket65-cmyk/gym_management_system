from django.urls import path, include
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter
from .views import (
    ProgramViewSet, TrainerViewSet, TrialBookingViewSet,
    MemberViewSet, MembershipPlanViewSet, SubscriptionViewSet,
    PaymentViewSet, AttendanceViewSet, ClassScheduleViewSet
)

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'trial-bookings', TrialBookingViewSet)
router.register(r'members', MemberViewSet)
router.register(r'membership-plans', MembershipPlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'class-schedules', ClassScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
