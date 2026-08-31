from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q, Sum, Count, F
from .models import Member, Trainer, MembershipPlan, Subscription, ClassSchedule, Attendance, WorkoutPlan, WorkoutExercise, Exercise, DietPlan, DietMeal, Appointment, InventoryItem, Expense, Staff, Notification, Payment, TrialBooking
from .forms import MemberForm, TrainerForm, MembershipPlanForm, ClassScheduleForm, AttendanceForm, WorkoutPlanForm, WorkoutExerciseForm, DietPlanForm, DietMealForm, AppointmentForm, InventoryItemForm, ExpenseForm, StaffForm, NotificationForm, TrialBookingForm
from .views import AdminProtectedTemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminProtectedMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/login/'
    
    def test_func(self):
        return self.request.user.is_superuser

class MemberListView(AdminProtectedMixin, ListView):
    model = Member
    template_name = "core/admin/members.html"
    context_object_name = "members"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Member.objects.all().order_by('-joined_date', '-id')
        
        # Search
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(email__icontains=q) |
                Q(phone__icontains=q)
            )
            
        # Filter by status
        status = self.request.GET.get('status')
        if status and status != 'All':
            queryset = queryset.filter(status=status)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', 'All')
        context['status_choices'] = Member.STATUS_CHOICES
        return context

class MemberCreateView(AdminProtectedMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = "core/admin/member_form.html"
    success_url = reverse_lazy('admin_members')

    def form_valid(self, form):
        messages.success(self.request, "Member created successfully.")
        return super().form_valid(form)

class MemberUpdateView(AdminProtectedMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = "core/admin/member_form.html"
    success_url = reverse_lazy('admin_members')

    def form_valid(self, form):
        messages.success(self.request, "Member updated successfully.")
        return super().form_valid(form)

class MemberDetailView(AdminProtectedMixin, DetailView):
    model = Member
    template_name = "core/admin/member_detail.html"
    context_object_name = "member"

    def get_queryset(self):
        return Member.objects.prefetch_related(
            'subscriptions__plan',
            'payments',
            'attendances',
            'workout_plans',
            'diet_plans',
            'appointments__trainer'
        )

class MemberDeleteView(AdminProtectedMixin, DeleteView):
    model = Member
    template_name = "core/admin/member_confirm_delete.html"
    success_url = reverse_lazy('admin_members')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Member deleted successfully.")
        return super().delete(request, *args, **kwargs)

class TrainerListView(AdminProtectedMixin, ListView):
    model = Trainer
    template_name = "core/admin/trainers.html"
    context_object_name = "trainers"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Trainer.objects.all().order_by('-created_at', '-id')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(full_name__icontains=q) |
                Q(role_specialty__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class TrainerCreateView(AdminProtectedMixin, CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "core/admin/trainer_form.html"
    success_url = reverse_lazy('admin_trainers')

    def form_valid(self, form):
        messages.success(self.request, "Trainer created successfully.")
        return super().form_valid(form)

class TrainerUpdateView(AdminProtectedMixin, UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "core/admin/trainer_form.html"
    success_url = reverse_lazy('admin_trainers')

    def form_valid(self, form):
        messages.success(self.request, "Trainer updated successfully.")
        return super().form_valid(form)

class TrainerDetailView(AdminProtectedMixin, DetailView):
    model = Trainer
    template_name = "core/admin/trainer_detail.html"
    context_object_name = "trainer"

    def get_queryset(self):
        return Trainer.objects.prefetch_related(
            'schedules',
            'appointments__member'
        )

class TrainerDeleteView(AdminProtectedMixin, DeleteView):
    model = Trainer
    template_name = "core/admin/trainer_confirm_delete.html"
    success_url = reverse_lazy('admin_trainers')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Trainer deleted successfully.")
        return super().delete(request, *args, **kwargs)

class MembershipPlanListView(AdminProtectedMixin, ListView):
    model = MembershipPlan
    template_name = "core/admin/plans.html"
    context_object_name = "plans"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = MembershipPlan.objects.all().order_by('-id')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(plan_name__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class MembershipPlanCreateView(AdminProtectedMixin, CreateView):
    model = MembershipPlan
    form_class = MembershipPlanForm
    template_name = "core/admin/plan_form.html"
    success_url = reverse_lazy('admin_plans')

    def form_valid(self, form):
        messages.success(self.request, "Membership plan created successfully.")
        return super().form_valid(form)

class MembershipPlanUpdateView(AdminProtectedMixin, UpdateView):
    model = MembershipPlan
    form_class = MembershipPlanForm
    template_name = "core/admin/plan_form.html"
    success_url = reverse_lazy('admin_plans')

    def form_valid(self, form):
        messages.success(self.request, "Membership plan updated successfully.")
        return super().form_valid(form)

class MembershipPlanDetailView(AdminProtectedMixin, DetailView):
    model = MembershipPlan
    template_name = "core/admin/plan_detail.html"
    context_object_name = "plan"

    def get_queryset(self):
        return MembershipPlan.objects.prefetch_related(
            'subscription_set__member'
        )

class MembershipPlanDeleteView(AdminProtectedMixin, DeleteView):
    model = MembershipPlan
    template_name = "core/admin/plan_confirm_delete.html"
    success_url = reverse_lazy('admin_plans')

    def delete(self, request, *args, **kwargs):
        plan = self.get_object()
        if plan.subscription_set.exists():
            messages.error(self.request, "Cannot delete plan: It is currently linked to one or more subscriptions. The model lacks an 'inactive' status, so deleting this would cascade and destroy historical subscription/payment data.")
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect(reverse_lazy('admin_plan_detail', kwargs={'pk': plan.id}))
            
        messages.success(self.request, "Membership plan deleted successfully.")
        return super().delete(request, *args, **kwargs)

class ClassScheduleListView(AdminProtectedMixin, ListView):
    model = ClassSchedule
    template_name = "core/admin/classes.html"
    context_object_name = "classes"
    paginate_by = 10

    def get_queryset(self):
        queryset = ClassSchedule.objects.select_related('program', 'trainer').order_by('day_of_week', 'start_time')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(class_name__icontains=q) |
                Q(program__title__icontains=q) |
                Q(trainer__full_name__icontains=q)
            )
        
        day = self.request.GET.get('day')
        if day and day != 'All':
            queryset = queryset.filter(day_of_week=day)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_day'] = self.request.GET.get('day', 'All')
        context['days'] = [c[0] for c in ClassSchedule.DAY_OF_WEEK_CHOICES]
        return context

class ClassScheduleCreateView(AdminProtectedMixin, CreateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "core/admin/class_form.html"
    success_url = reverse_lazy('admin_classes')

    def form_valid(self, form):
        messages.success(self.request, "Class created successfully.")
        return super().form_valid(form)

class ClassScheduleUpdateView(AdminProtectedMixin, UpdateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "core/admin/class_form.html"
    success_url = reverse_lazy('admin_classes')

    def form_valid(self, form):
        messages.success(self.request, "Class updated successfully.")
        return super().form_valid(form)

class ClassScheduleDetailView(AdminProtectedMixin, DetailView):
    model = ClassSchedule
    template_name = "core/admin/class_detail.html"
    context_object_name = "class_obj"

    def get_queryset(self):
        return ClassSchedule.objects.select_related('program', 'trainer')

class ClassScheduleDeleteView(AdminProtectedMixin, DeleteView):
    model = ClassSchedule
    template_name = "core/admin/class_confirm_delete.html"
    success_url = reverse_lazy('admin_classes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Class deleted successfully.")
        return super().delete(request, *args, **kwargs)

class AttendanceListView(AdminProtectedMixin, ListView):
    model = Attendance
    template_name = "core/admin/attendance.html"
    context_object_name = "attendances"
    paginate_by = 10

    def get_queryset(self):
        queryset = Attendance.objects.select_related('member').order_by('-check_in_time', '-id')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(member__first_name__icontains=q) |
                Q(member__last_name__icontains=q) |
                Q(member__email__icontains=q)
            )
            
        date_filter = self.request.GET.get('date')
        if date_filter:
            queryset = queryset.filter(check_in_time__date=date_filter)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['date_filter'] = self.request.GET.get('date', '')
        return context

class AttendanceCreateView(AdminProtectedMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "core/admin/attendance_form.html"
    success_url = reverse_lazy('admin_attendance')

    def form_valid(self, form):
        messages.success(self.request, "Attendance record created successfully.")
        return super().form_valid(form)

class AttendanceUpdateView(AdminProtectedMixin, UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "core/admin/attendance_form.html"
    success_url = reverse_lazy('admin_attendance')

    def form_valid(self, form):
        messages.success(self.request, "Attendance record updated successfully.")
        return super().form_valid(form)

class AttendanceDetailView(AdminProtectedMixin, DetailView):
    model = Attendance
    template_name = "core/admin/attendance_detail.html"
    context_object_name = "attendance"

    def get_queryset(self):
        return Attendance.objects.select_related('member')

class AttendanceDeleteView(AdminProtectedMixin, DeleteView):
    model = Attendance
    template_name = "core/admin/attendance_confirm_delete.html"
    success_url = reverse_lazy('admin_attendance')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Attendance record deleted successfully.")
        return super().delete(request, *args, **kwargs)

class WorkoutPlanListView(AdminProtectedMixin, ListView):
    model = WorkoutPlan
    template_name = "core/admin/workouts.html"
    context_object_name = "workouts"
    paginate_by = 10

    def get_queryset(self):
        from django.db.models import Count
        queryset = WorkoutPlan.objects.select_related('member', 'trainer').annotate(exercise_count=Count('exercises')).order_by('-created_at')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(goal__icontains=q) |
                Q(member__first_name__icontains=q) |
                Q(member__last_name__icontains=q) |
                Q(member__email__icontains=q) |
                Q(trainer__full_name__icontains=q)
            )
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['statuses'] = [c[0] for c in WorkoutPlan.STATUS_CHOICES]
        return context

class WorkoutPlanCreateView(AdminProtectedMixin, CreateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    template_name = "core/admin/workout_form.html"
    success_url = reverse_lazy('admin_workouts')

    def form_valid(self, form):
        messages.success(self.request, "Workout plan created successfully.")
        return super().form_valid(form)

class WorkoutPlanUpdateView(AdminProtectedMixin, UpdateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    template_name = "core/admin/workout_form.html"
    success_url = reverse_lazy('admin_workouts')

    def form_valid(self, form):
        messages.success(self.request, "Workout plan updated successfully.")
        return super().form_valid(form)

class WorkoutPlanDetailView(AdminProtectedMixin, DetailView):
    model = WorkoutPlan
    template_name = "core/admin/workout_detail.html"
    context_object_name = "workout"

    def get_queryset(self):
        return WorkoutPlan.objects.select_related('member', 'trainer').prefetch_related('exercises__exercise')

class WorkoutPlanDeleteView(AdminProtectedMixin, DeleteView):
    model = WorkoutPlan
    template_name = "core/admin/workout_confirm_delete.html"
    success_url = reverse_lazy('admin_workouts')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Workout plan deleted successfully.")
        return super().delete(request, *args, **kwargs)

class WorkoutExerciseCreateView(AdminProtectedMixin, CreateView):
    model = WorkoutExercise
    form_class = WorkoutExerciseForm
    template_name = "core/admin/workout_exercise_form.html"

    def form_valid(self, form):
        workout_plan = WorkoutPlan.objects.get(pk=self.kwargs['workout_pk'])
        form.instance.workout_plan = workout_plan
        messages.success(self.request, "Exercise added successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_workout_detail', kwargs={'pk': self.kwargs['workout_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout'] = WorkoutPlan.objects.get(pk=self.kwargs['workout_pk'])
        return context

class WorkoutExerciseUpdateView(AdminProtectedMixin, UpdateView):
    model = WorkoutExercise
    form_class = WorkoutExerciseForm
    template_name = "core/admin/workout_exercise_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Exercise updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_workout_detail', kwargs={'pk': self.kwargs['workout_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout'] = WorkoutPlan.objects.get(pk=self.kwargs['workout_pk'])
        return context

class WorkoutExerciseDeleteView(AdminProtectedMixin, DeleteView):
    model = WorkoutExercise
    template_name = "core/admin/workout_exercise_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Exercise removed successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin_workout_detail', kwargs={'pk': self.kwargs['workout_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout'] = WorkoutPlan.objects.get(pk=self.kwargs['workout_pk'])
        return context

class DietPlanListView(AdminProtectedMixin, ListView):
    model = DietPlan
    template_name = "core/admin/diet_plans.html"
    context_object_name = "diet_plans"
    paginate_by = 10

    def get_queryset(self):
        from django.db.models import Count
        queryset = DietPlan.objects.select_related('member', 'trainer').annotate(meal_count=Count('meals')).order_by('-created_at')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(goal__icontains=q) |
                Q(member__first_name__icontains=q) |
                Q(member__last_name__icontains=q) |
                Q(member__email__icontains=q) |
                Q(trainer__full_name__icontains=q)
            )
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['statuses'] = [c[0] for c in DietPlan.STATUS_CHOICES]
        return context

class DietPlanCreateView(AdminProtectedMixin, CreateView):
    model = DietPlan
    form_class = DietPlanForm
    template_name = "core/admin/diet_plan_form.html"
    success_url = reverse_lazy('admin_diet_plans')

    def form_valid(self, form):
        messages.success(self.request, "Diet plan created successfully.")
        return super().form_valid(form)

class DietPlanUpdateView(AdminProtectedMixin, UpdateView):
    model = DietPlan
    form_class = DietPlanForm
    template_name = "core/admin/diet_plan_form.html"
    success_url = reverse_lazy('admin_diet_plans')

    def form_valid(self, form):
        messages.success(self.request, "Diet plan updated successfully.")
        return super().form_valid(form)

class DietPlanDetailView(AdminProtectedMixin, DetailView):
    model = DietPlan
    template_name = "core/admin/diet_plan_detail.html"
    context_object_name = "diet_plan"

    def get_queryset(self):
        return DietPlan.objects.select_related('member', 'trainer').prefetch_related('meals')

class DietPlanDeleteView(AdminProtectedMixin, DeleteView):
    model = DietPlan
    template_name = "core/admin/diet_plan_confirm_delete.html"
    success_url = reverse_lazy('admin_diet_plans')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Diet plan deleted successfully.")
        return super().delete(request, *args, **kwargs)

class DietMealCreateView(AdminProtectedMixin, CreateView):
    model = DietMeal
    form_class = DietMealForm
    template_name = "core/admin/diet_meal_form.html"

    def form_valid(self, form):
        diet_plan = DietPlan.objects.get(pk=self.kwargs['plan_pk'])
        form.instance.diet_plan = diet_plan
        messages.success(self.request, "Meal added successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_diet_plan_detail', kwargs={'pk': self.kwargs['plan_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diet_plan'] = DietPlan.objects.get(pk=self.kwargs['plan_pk'])
        return context

class DietMealUpdateView(AdminProtectedMixin, UpdateView):
    model = DietMeal
    form_class = DietMealForm
    template_name = "core/admin/diet_meal_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Meal updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_diet_plan_detail', kwargs={'pk': self.kwargs['plan_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diet_plan'] = DietPlan.objects.get(pk=self.kwargs['plan_pk'])
        return context

class DietMealDeleteView(AdminProtectedMixin, DeleteView):
    model = DietMeal
    template_name = "core/admin/diet_meal_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Meal removed successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin_diet_plan_detail', kwargs={'pk': self.kwargs['plan_pk']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diet_plan'] = DietPlan.objects.get(pk=self.kwargs['plan_pk'])
        return context

# ----------------- APPOINTMENTS ----------------- #

class AppointmentListView(AdminProtectedMixin, ListView):
    model = Appointment
    template_name = "core/admin/appointments.html"
    context_object_name = "appointments"
    paginate_by = 10

    def get_queryset(self):
        queryset = Appointment.objects.select_related('member', 'trainer').order_by('-appointment_date', '-start_time')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(member__first_name__icontains=q) |
                Q(member__last_name__icontains=q) |
                Q(member__email__icontains=q) |
                Q(trainer__full_name__icontains=q) |
                Q(appointment_type__icontains=q)
            )
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        appt_type = self.request.GET.get('type')
        if appt_type:
            queryset = queryset.filter(appointment_type=appt_type)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_type'] = self.request.GET.get('type', '')
        # Get unique types and statuses for the filters
        context['types'] = Appointment.objects.values_list('appointment_type', flat=True).distinct()
        context['statuses'] = Appointment.objects.values_list('status', flat=True).distinct()
        return context

class AppointmentCreateView(AdminProtectedMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "core/admin/appointment_form.html"
    success_url = reverse_lazy('admin_appointments')

    def form_valid(self, form):
        if form.cleaned_data['start_time'] and form.cleaned_data['end_time']:
            if form.cleaned_data['end_time'] <= form.cleaned_data['start_time']:
                form.add_error('end_time', "End time must be after start time.")
                return self.form_invalid(form)
        messages.success(self.request, "Appointment created successfully.")
        return super().form_valid(form)

class AppointmentUpdateView(AdminProtectedMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "core/admin/appointment_form.html"
    success_url = reverse_lazy('admin_appointments')

    def form_valid(self, form):
        if form.cleaned_data['start_time'] and form.cleaned_data['end_time']:
            if form.cleaned_data['end_time'] <= form.cleaned_data['start_time']:
                form.add_error('end_time', "End time must be after start time.")
                return self.form_invalid(form)
        messages.success(self.request, "Appointment updated successfully.")
        return super().form_valid(form)

class AppointmentDetailView(AdminProtectedMixin, DetailView):
    model = Appointment
    template_name = "core/admin/appointment_detail.html"
    context_object_name = "appointment"

    def get_queryset(self):
        return Appointment.objects.select_related('member', 'trainer')

class AppointmentDeleteView(AdminProtectedMixin, DeleteView):
    model = Appointment
    template_name = "core/admin/appointment_confirm_delete.html"
    success_url = reverse_lazy('admin_appointments')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Appointment deleted successfully.")
        return super().delete(request, *args, **kwargs)

# ----------------- INVENTORY ----------------- #

class InventoryListView(AdminProtectedMixin, ListView):
    model = InventoryItem
    template_name = "core/admin/inventory.html"
    context_object_name = "inventory"
    paginate_by = 10

    def get_queryset(self):
        from django.db.models import F
        queryset = InventoryItem.objects.all().order_by('item_name')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(item_name__icontains=q) |
                Q(sku__icontains=q) |
                Q(supplier__icontains=q) |
                Q(category__icontains=q)
            )
            
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        stock = self.request.GET.get('stock')
        if stock == 'low':
            queryset = queryset.filter(quantity__lte=F('min_stock_level'))
        elif stock == 'in_stock':
            queryset = queryset.filter(quantity__gt=F('min_stock_level'))
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_stock'] = self.request.GET.get('stock', '')
        context['categories'] = InventoryItem.objects.values_list('category', flat=True).distinct()
        context['statuses'] = InventoryItem.objects.values_list('status', flat=True).distinct()
        return context

class InventoryCreateView(AdminProtectedMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = "core/admin/inventory_form.html"
    success_url = reverse_lazy('admin_inventory')

    def form_valid(self, form):
        if form.cleaned_data['quantity'] < 0:
            form.add_error('quantity', "Quantity cannot be negative.")
            return self.form_invalid(form)
        if form.cleaned_data['min_stock_level'] < 0:
            form.add_error('min_stock_level', "Min stock level cannot be negative.")
            return self.form_invalid(form)
        if form.cleaned_data['purchase_price'] < 0:
            form.add_error('purchase_price', "Purchase price cannot be negative.")
            return self.form_invalid(form)
        messages.success(self.request, "Inventory item created successfully.")
        return super().form_valid(form)

class InventoryUpdateView(AdminProtectedMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = "core/admin/inventory_form.html"
    success_url = reverse_lazy('admin_inventory')

    def form_valid(self, form):
        if form.cleaned_data['quantity'] < 0:
            form.add_error('quantity', "Quantity cannot be negative.")
            return self.form_invalid(form)
        if form.cleaned_data['min_stock_level'] < 0:
            form.add_error('min_stock_level', "Min stock level cannot be negative.")
            return self.form_invalid(form)
        if form.cleaned_data['purchase_price'] < 0:
            form.add_error('purchase_price', "Purchase price cannot be negative.")
            return self.form_invalid(form)
        messages.success(self.request, "Inventory item updated successfully.")
        return super().form_valid(form)

class InventoryDetailView(AdminProtectedMixin, DetailView):
    model = InventoryItem
    template_name = "core/admin/inventory_detail.html"
    context_object_name = "item"

class InventoryDeleteView(AdminProtectedMixin, DeleteView):
    model = InventoryItem
    template_name = "core/admin/inventory_confirm_delete.html"
    success_url = reverse_lazy('admin_inventory')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Inventory item deleted successfully.")
        return super().delete(request, *args, **kwargs)

# ----------------- EXPENSES ----------------- #

class ExpenseListView(AdminProtectedMixin, ListView):
    model = Expense
    template_name = "core/admin/expenses.html"
    context_object_name = "expenses"
    paginate_by = 10

    def get_queryset(self):
        queryset = Expense.objects.select_related('recorded_by').order_by('-expense_date', '-created_at')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(category__icontains=q) |
                Q(description__icontains=q) |
                Q(reference__icontains=q)
            )
            
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
            
        method = self.request.GET.get('method')
        if method:
            queryset = queryset.filter(payment_method=method)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_method'] = self.request.GET.get('method', '')
        context['categories'] = Expense.objects.values_list('category', flat=True).distinct()
        context['methods'] = Expense.objects.values_list('payment_method', flat=True).distinct()
        return context

class ExpenseCreateView(AdminProtectedMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "core/admin/expense_form.html"
    success_url = reverse_lazy('admin_expenses')

    def form_valid(self, form):
        if form.cleaned_data['amount'] <= 0:
            form.add_error('amount', "Amount must be greater than zero.")
            return self.form_invalid(form)
        messages.success(self.request, "Expense recorded successfully.")
        return super().form_valid(form)

class ExpenseUpdateView(AdminProtectedMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "core/admin/expense_form.html"
    success_url = reverse_lazy('admin_expenses')

    def form_valid(self, form):
        if form.cleaned_data['amount'] <= 0:
            form.add_error('amount', "Amount must be greater than zero.")
            return self.form_invalid(form)
        messages.success(self.request, "Expense updated successfully.")
        return super().form_valid(form)

class ExpenseDetailView(AdminProtectedMixin, DetailView):
    model = Expense
    template_name = "core/admin/expense_detail.html"
    context_object_name = "expense"

    def get_queryset(self):
        return Expense.objects.select_related('recorded_by')

class ExpenseDeleteView(AdminProtectedMixin, DeleteView):
    model = Expense
    template_name = "core/admin/expense_confirm_delete.html"
    success_url = reverse_lazy('admin_expenses')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Expense deleted successfully.")
        return super().delete(request, *args, **kwargs)

# ----------------- STAFF ----------------- #

class StaffListView(AdminProtectedMixin, ListView):
    model = Staff
    template_name = "core/admin/staff.html"
    context_object_name = "staff_members"
    paginate_by = 10

    def get_queryset(self):
        queryset = Staff.objects.select_related('user').order_by('-joining_date')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(user__first_name__icontains=q) |
                Q(user__last_name__icontains=q) |
                Q(user__email__icontains=q) |
                Q(user__username__icontains=q) |
                Q(phone__icontains=q) |
                Q(role__icontains=q)
            )
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        role = self.request.GET.get('role')
        if role:
            queryset = queryset.filter(role=role)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_role'] = self.request.GET.get('role', '')
        context['statuses'] = Staff.objects.values_list('status', flat=True).distinct()
        context['roles'] = Staff.objects.values_list('role', flat=True).distinct()
        return context

class StaffCreateView(AdminProtectedMixin, CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "core/admin/staff_form.html"
    success_url = reverse_lazy('admin_staff')

    def form_valid(self, form):
        messages.success(self.request, "Staff member created successfully.")
        return super().form_valid(form)

class StaffUpdateView(AdminProtectedMixin, UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = "core/admin/staff_form.html"
    success_url = reverse_lazy('admin_staff')

    def form_valid(self, form):
        messages.success(self.request, "Staff member updated successfully.")
        return super().form_valid(form)

class StaffDetailView(AdminProtectedMixin, DetailView):
    model = Staff
    template_name = "core/admin/staff_detail.html"
    context_object_name = "staff"

    def get_queryset(self):
        return Staff.objects.select_related('user')

class StaffDeleteView(AdminProtectedMixin, DeleteView):
    model = Staff
    template_name = "core/admin/staff_confirm_delete.html"
    success_url = reverse_lazy('admin_staff')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Staff member removed successfully.")
        return super().delete(request, *args, **kwargs)

# ----------------- NOTIFICATIONS ----------------- #

class NotificationListView(AdminProtectedMixin, ListView):
    model = Notification
    template_name = "core/admin/notifications.html"
    context_object_name = "notifications"
    paginate_by = 10

    def get_queryset(self):
        queryset = Notification.objects.select_related('recipient').order_by('-created_at')
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(message__icontains=q) |
                Q(recipient__username__icontains=q) |
                Q(recipient__email__icontains=q)
            )
            
        notification_type = self.request.GET.get('type')
        if notification_type:
            queryset = queryset.filter(notification_type=notification_type)
            
        is_read = self.request.GET.get('is_read')
        if is_read == 'true':
            queryset = queryset.filter(is_read=True)
        elif is_read == 'false':
            queryset = queryset.filter(is_read=False)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['current_type'] = self.request.GET.get('type', '')
        context['current_is_read'] = self.request.GET.get('is_read', '')
        context['types'] = Notification.objects.values_list('notification_type', flat=True).distinct()
        return context

class NotificationCreateView(AdminProtectedMixin, CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = "core/admin/notification_form.html"
    success_url = reverse_lazy('admin_notifications')

    def form_valid(self, form):
        messages.success(self.request, "Notification sent successfully.")
        return super().form_valid(form)

class NotificationUpdateView(AdminProtectedMixin, UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = "core/admin/notification_form.html"
    success_url = reverse_lazy('admin_notifications')

    def form_valid(self, form):
        messages.success(self.request, "Notification updated successfully.")
        return super().form_valid(form)

class NotificationDetailView(AdminProtectedMixin, DetailView):
    model = Notification
    template_name = "core/admin/notification_detail.html"
    context_object_name = "notification"

    def get_queryset(self):
        return Notification.objects.select_related('recipient')

class NotificationDeleteView(AdminProtectedMixin, DeleteView):
    model = Notification
    template_name = "core/admin/notification_confirm_delete.html"
    success_url = reverse_lazy('admin_notifications')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Notification deleted successfully.")
        return super().delete(request, *args, **kwargs)

class NotificationReadView(AdminProtectedMixin, View):
    def post(self, request, pk, *args, **kwargs):
        notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
        notification.is_read = not notification.is_read
        notification.save()
        return redirect('admin_notifications')

class TrialBookingListView(AdminProtectedMixin, ListView):
    model = TrialBooking
    template_name = 'core/admin/trial_bookings.html'
    context_object_name = 'object_list'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        status = self.request.GET.get('status')
        if query:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query) |
                Q(program__title__icontains=query)
            )
        if status:
            qs = qs.filter(status=status)
        return qs
        
class TrialBookingDetailView(AdminProtectedMixin, DetailView):
    model = TrialBooking
    template_name = 'core/admin/trial_booking_detail.html'
    context_object_name = 'object'

class TrialBookingCreateView(AdminProtectedMixin, CreateView):
    model = TrialBooking
    form_class = TrialBookingForm
    template_name = 'core/admin/trial_booking_form.html'
    success_url = reverse_lazy('admin_trial_bookings')

    def form_valid(self, form):
        messages.success(self.request, "Trial booking created successfully.")
        return super().form_valid(form)

class TrialBookingUpdateView(AdminProtectedMixin, UpdateView):
    model = TrialBooking
    form_class = TrialBookingForm
    template_name = 'core/admin/trial_booking_form.html'
    success_url = reverse_lazy('admin_trial_bookings')

    def form_valid(self, form):
        messages.success(self.request, "Trial booking updated successfully.")
        return super().form_valid(form)

class TrialBookingDeleteView(AdminProtectedMixin, DeleteView):
    model = TrialBooking
    template_name = 'core/admin/trial_booking_confirm_delete.html'
    success_url = reverse_lazy('admin_trial_bookings')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Trial booking deleted successfully.")
        return super().delete(request, *args, **kwargs)

# ----------------- REPORTS ----------------- #

import datetime
from django.utils import timezone
from decimal import Decimal

class ReportsDashboardView(AdminProtectedMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        
        # Get date filters
        from_date_str = request.GET.get('from_date')
        to_date_str = request.GET.get('to_date')
        
        # Base querysets
        payments = Payment.objects.filter(payment_status='Completed')
        expenses = Expense.objects.all()
        members = Member.objects.all()
        attendance = Attendance.objects.all()
        appointments = Appointment.objects.all()
        
        if from_date_str:
            try:
                from_date = datetime.datetime.strptime(from_date_str, "%Y-%m-%d").date()
                payments = payments.filter(transaction_date__date__gte=from_date)
                expenses = expenses.filter(expense_date__gte=from_date)
                attendance = attendance.filter(date__gte=from_date)
                appointments = appointments.filter(appointment_date__gte=from_date)
            except ValueError:
                pass
                
        if to_date_str:
            try:
                to_date = datetime.datetime.strptime(to_date_str, "%Y-%m-%d").date()
                payments = payments.filter(transaction_date__date__lte=to_date)
                expenses = expenses.filter(expense_date__lte=to_date)
                attendance = attendance.filter(date__lte=to_date)
                appointments = appointments.filter(appointment_date__lte=to_date)
            except ValueError:
                pass

        # 1. Revenue Report
        revenue_total = payments.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        payment_count = payments.count()
        context['revenue'] = {
            'total': revenue_total,
            'count': payment_count,
            'average': revenue_total / payment_count if payment_count > 0 else Decimal('0.00')
        }
        
        # 2. Expense Report
        expense_total = expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        expense_count = expenses.count()
        context['expense'] = {
            'total': expense_total,
            'count': expense_count,
            'by_category': list(expenses.values('category').annotate(total=Sum('amount'), count=Count('id')).order_by('-total'))
        }
        
        # 3. Profit Report
        context['profit'] = {
            'net_profit': revenue_total - expense_total
        }
        
        # 4. Membership Report
        active_members = members.filter(status='Active').count()
        inactive_members = members.filter(status='Inactive').count()
        context['members'] = {
            'total': members.count(),
            'active': active_members,
            'inactive': inactive_members,
            'by_plan': list(Subscription.objects.filter(status='Active').values('plan__plan_name').annotate(count=Count('id')).order_by('-count'))
        }
        
        # 5. Attendance Report
        today = timezone.now().date()
        context['attendance'] = {
            'today': Attendance.objects.filter(date=today).count(),
            'total_period': attendance.count()
        }
        
        # 6. Trainer Report
        context['trainers'] = {
            'total': Trainer.objects.count()
        }
        
        # 7. Appointment Report
        context['appointments'] = {
            'total': appointments.count(),
            'scheduled': appointments.filter(status='Scheduled').count(),
            'completed': appointments.filter(status='Completed').count(),
            'cancelled': appointments.filter(status='Cancelled').count(),
        }
        
        # 8. Inventory Report
        inventory = InventoryItem.objects.all()
        low_stock = inventory.filter(quantity__lte=F('min_stock_level')).count()
        
        # Calculate total value in Python to handle types safely or via expression
        from django.db.models import ExpressionWrapper, DecimalField
        total_value_calc = inventory.annotate(
            val=ExpressionWrapper(F('quantity') * F('purchase_price'), output_field=DecimalField())
        ).aggregate(total=Sum('val'))['total'] or Decimal('0.00')
        
        context['inventory'] = {
            'total_items': inventory.count(),
            'low_stock': low_stock,
            'total_value': total_value_calc
        }

        # Chart Data Preparation (JSON)
        
        # Revenue by month (last 6 months approximation)
        context['chart_revenue_by_month'] = []
        # We will let JS handle the empty state, just provide the data we can aggregate simply.
        # SQLite doesn't natively do TruncMonth easily without specific functions, we'll do simple aggregation if we must, or just pass raw data.
        # For simplicity and DB agnosticism, let's aggregate in Python if the dataset is small, but standard Django handles it.
        from django.db.models.functions import TruncMonth
        monthly_revenue = Payment.objects.filter(payment_status='Completed').annotate(month=TruncMonth('transaction_date')).values('month').annotate(total=Sum('amount')).order_by('month')
        rev_data = []
        for mr in monthly_revenue:
            if mr['month']:
                rev_data.append({'month': mr['month'].strftime('%Y-%m'), 'total': str(mr['total'])})
        context['chart_revenue'] = rev_data

        monthly_expense = Expense.objects.annotate(month=TruncMonth('expense_date')).values('month').annotate(total=Sum('amount')).order_by('month')
        exp_data = []
        for me in monthly_expense:
            if me['month']:
                exp_data.append({'month': me['month'].strftime('%Y-%m'), 'total': str(me['total'])})
        context['chart_expense'] = exp_data

        return render(request, 'core/admin/reports.html', context)
