from django.contrib import admin
from .models import (
    Program, Trainer, TrialBooking, Member, MembershipPlan,
    Subscription, Payment, Attendance, ClassSchedule
)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role_specialty', 'created_at')
    list_filter = ('role_specialty',)
    search_fields = ('full_name', 'role_specialty')

@admin.register(TrialBooking)
class TrialBookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'program')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'status', 'joined_date')
    list_filter = ('status', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'duration_months', 'price')
    search_fields = ('plan_name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'plan')
    search_fields = ('member__first_name', 'member__last_name', 'member__email')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'payment_method', 'payment_status', 'transaction_date')
    list_filter = ('payment_status', 'payment_method')
    search_fields = ('member__first_name', 'member__last_name', 'member__email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'check_in_time', 'check_out_time')
    list_filter = ('check_in_time',)
    search_fields = ('member__first_name', 'member__last_name', 'member__email')

@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'program', 'trainer', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('day_of_week', 'program', 'trainer')
    search_fields = ('class_name',)


from .models import (
    Exercise, WorkoutPlan, WorkoutExercise, DietPlan, DietMeal,
    Appointment, InventoryItem, Expense, Staff, Notification
)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_muscle', 'difficulty', 'created_at')
    search_fields = ('name', 'target_muscle')
    list_filter = ('difficulty',)

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'trainer', 'start_date', 'end_date', 'status')
    search_fields = ('name', 'member__first_name', 'member__last_name', 'trainer__full_name')
    list_filter = ('status',)

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'workout_plan', 'sets', 'repetitions', 'weight', 'order')
    search_fields = ('exercise__name', 'workout_plan__name')

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'trainer', 'start_date', 'end_date', 'status', 'daily_calories')
    search_fields = ('name', 'member__first_name', 'member__last_name', 'trainer__full_name')
    list_filter = ('status',)

@admin.register(DietMeal)
class DietMealAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'diet_plan', 'meal_time', 'calories', 'order')
    search_fields = ('meal_type', 'diet_plan__name', 'food_description')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_type', 'member', 'trainer', 'appointment_date', 'start_time', 'status')
    search_fields = ('appointment_type', 'member__first_name', 'member__last_name', 'trainer__full_name')
    list_filter = ('status', 'appointment_date')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'sku', 'category', 'quantity', 'min_stock_level', 'status')
    search_fields = ('item_name', 'sku', 'category')
    list_filter = ('status', 'category')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'expense_date', 'payment_method')
    search_fields = ('category', 'description', 'reference')
    list_filter = ('category', 'expense_date', 'payment_method')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'joining_date', 'status')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'role')
    list_filter = ('status', 'role')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient', 'notification_type', 'is_read', 'created_at')
    search_fields = ('title', 'recipient__username', 'message')
    list_filter = ('is_read', 'notification_type')
