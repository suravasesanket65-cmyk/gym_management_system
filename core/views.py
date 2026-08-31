from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.db import transaction
# pyrefly: ignore [missing-import]
from rest_framework import viewsets, mixins
from .models import (
    Program, Trainer, TrialBooking, Member, MembershipPlan,
    Subscription, Payment, Attendance, ClassSchedule, Notification
)
from .forms import PublicRegistrationForm, PublicTrialBookingForm
from .serializers import (
    ProgramSerializer, TrainerSerializer, TrialBookingSerializer,
    MemberSerializer, MembershipPlanSerializer, SubscriptionSerializer,
    PaymentSerializer, AttendanceSerializer, ClassScheduleSerializer
)

def home_page(request):
    """
    Renders the main monolithic landing page HTML template.
    """
    programs = Program.objects.all()
    return render(request, 'core/index.html', {'programs': programs})


def login_view(request):
    """
    Handles both GET and POST requests for the Glassmorphism login page.
    Authenticates the user and redirects them based on their role.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            
    return render(request, 'core/login.html')


def register_page(request):
    """
    Handles user registration and renders the registration page.
    """
    if request.method == 'POST':
        form = PublicRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, 'core/register.html', {'form': form})
                
            if Member.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return render(request, 'core/register.html', {'form': form})

            try:
                with transaction.atomic():
                    # Create the Django User
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=form.cleaned_data['password'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name']
                    )
                    
                    # Create the Member profile
                    from datetime import date
                    Member.objects.create(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=email,
                        phone=form.cleaned_data['phone'],
                        gender="O",
                        date_of_birth=date(2000, 1, 1),
                        status="Active"
                    )
                    
                    # Notify admins
                    admin_users = User.objects.filter(is_superuser=True)
                    for admin_user in admin_users:
                        Notification.objects.create(
                            recipient=admin_user,
                            title="New Member Registration",
                            message=f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']} has registered.",
                            notification_type="System"
                        )
                    
                login(request, user)
                messages.success(request, "Thank you! Your registration has been received successfully.")
                return redirect('home')
                
            except Exception as e:
                messages.error(request, f"Registration failed. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PublicRegistrationForm()
            
    return render(request, 'core/register.html', {'form': form})

@require_POST
def submit_trial_booking(request):
    """
    Handles trial booking / enquiry submissions from the public landing page.
    """
    form = PublicTrialBookingForm(request.POST)
    if form.is_valid():
        try:
            with transaction.atomic():
                trial = form.save(commit=False)
                trial.status = 'New'
                trial.save()
                
                # Notify admins
                admin_users = User.objects.filter(is_superuser=True)
                for admin_user in admin_users:
                    Notification.objects.create(
                        recipient=admin_user,
                        title="New Trial Booking / Enquiry",
                        message=f"{trial.first_name} {trial.last_name} requested a trial for {trial.program}.",
                        notification_type="System"
                    )
            
            messages.success(request, "Thank you for contacting CORESA Gym. Your enquiry has been received successfully.")
        except Exception as e:
            messages.error(request, "Submission failed. Please try again.")
    else:
        messages.error(request, "Please check your form inputs and try again.")
    return redirect('home')

class AdminProtectedTemplateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    Base view for all Admin Dashboard templates.
    Ensures the user is logged in and is a superuser.
    """
    login_url = '/login/'
    
    def test_func(self):
        return self.request.user.is_superuser

from core.services.dashboard_service import DashboardService

class DashboardHomeView(AdminProtectedTemplateView):
    template_name = "core/admin/dashboard_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get KPIs
        context.update(DashboardService.get_kpis())
        
        # Get Recent Members
        context['latest_members'] = DashboardService.get_recent_members()
        
        # Get Upcoming Appointments
        context['upcoming_appointments_list'] = DashboardService.get_upcoming_appointments_table()
        
        # Get Chart Data
        context['revenue_attendance_chart'] = DashboardService.get_revenue_attendance_chart()
        context['membership_distribution'] = DashboardService.get_membership_distribution()
        
        return context

class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public endpoint to list all available workout programs.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class TrainerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public endpoint to list all trainers.
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer



class TrialBookingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Public endpoint for frontend landing page form submissions.
    """
    queryset = TrialBooking.objects.all()
    serializer_class = TrialBookingSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for Members.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MembershipPlanViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for MembershipPlans.
    """
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for Subscriptions.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for Payments.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for Attendance check-ins.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class ClassScheduleViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoints for ClassSchedules.
    """
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer
