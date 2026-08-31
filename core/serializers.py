# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import (
    Program, Trainer, TrialBooking, Member, MembershipPlan,
    Subscription, Payment, Attendance, ClassSchedule
)

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class TrialBookingSerializer(serializers.ModelSerializer):
    program_details = ProgramSerializer(source='program', read_only=True)

    class Meta:
        model = TrialBooking
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    plan_details = MembershipPlanSerializer(source='plan', read_only=True)
    
    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class ClassScheduleSerializer(serializers.ModelSerializer):
    program_details = ProgramSerializer(source='program', read_only=True)
    trainer_details = TrainerSerializer(source='trainer', read_only=True)

    class Meta:
        model = ClassSchedule
        fields = '__all__'
