from django import forms
from .models import Member, Trainer, MembershipPlan, ClassSchedule, Attendance, WorkoutPlan, WorkoutExercise, Exercise, DietPlan, DietMeal, Appointment, InventoryItem, Expense, Staff, Notification, TrialBooking

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 'last_name', 'email', 'phone', 
            'gender', 'date_of_birth', 'address', 
            'emergency_contact', 'status'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Full Address'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Emergency Contact Info'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'full_name', 'role_specialty', 'image_url',
            'instagram_url', 'linkedin_url'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full Name'}),
            'role_specialty': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Role / Specialty'}),
            'image_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Image URL'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Instagram URL'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'LinkedIn URL'}),
        }

class MembershipPlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['plan_name', 'duration_months', 'price', 'description']
        widgets = {
            'plan_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Plan Name'}),
            'duration_months': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Duration (Months)'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Price ($)', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Plan Description / Features'}),
        }

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['class_name', 'program', 'trainer', 'day_of_week', 'start_time', 'end_time', 'max_capacity']
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Class Name'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
            'day_of_week': forms.Select(attrs={'class': 'form-select'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'max_capacity': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Max Capacity'}),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'check_in_time', 'check_out_time']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-select'}),
            'check_in_time': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'check_out_time': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
        }

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['member', 'trainer', 'name', 'goal', 'start_date', 'end_date', 'status', 'notes']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Workout Plan Name'}),
            'goal': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Goal (e.g., Weight Loss)'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Additional Notes'}),
        }

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'repetitions', 'weight', 'duration', 'rest_time', 'order', 'notes']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-select'}),
            'sets': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Sets'}),
            'repetitions': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Repetitions (e.g., 10-12)'}),
            'weight': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Weight (kg/lbs)', 'step': '0.01'}),
            'duration': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Duration (seconds)'}),
            'rest_time': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Rest Time (seconds)'}),
            'order': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Order (e.g., 1)'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': 'Execution Notes'}),
        }

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['member', 'trainer', 'name', 'goal', 'daily_calories', 'start_date', 'end_date', 'status', 'notes']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Diet Plan Name'}),
            'goal': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Goal (e.g., Muscle Gain)'}),
            'daily_calories': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Daily Calories', 'step': '0.01'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Additional Notes'}),
        }

class DietMealForm(forms.ModelForm):
    class Meta:
        model = DietMeal
        fields = ['meal_type', 'meal_time', 'food_description', 'calories', 'protein', 'carbohydrates', 'fats', 'notes', 'order']
        widgets = {
            'meal_type': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Meal Type (e.g., Breakfast)'}),
            'meal_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'food_description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Food Description'}),
            'calories': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Calories', 'step': '0.01'}),
            'protein': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Protein (g)', 'step': '0.01'}),
            'carbohydrates': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Carbs (g)', 'step': '0.01'}),
            'fats': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Fats (g)', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': 'Additional Notes'}),
            'order': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Order'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['member', 'trainer', 'appointment_date', 'start_time', 'end_time', 'appointment_type', 'status', 'notes']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
            'appointment_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'appointment_type': forms.TextInput(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['item_name', 'category', 'sku', 'quantity', 'min_stock_level', 'unit', 'purchase_price', 'supplier', 'location', 'status']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-input'}),
            'category': forms.TextInput(attrs={'class': 'form-input'}),
            'sku': forms.TextInput(attrs={'class': 'form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input'}),
            'min_stock_level': forms.NumberInput(attrs={'class': 'form-input'}),
            'unit': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., kg, pcs'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'supplier': forms.TextInput(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'expense_date', 'description', 'payment_method', 'reference', 'recorded_by']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'expense_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'payment_method': forms.TextInput(attrs={'class': 'form-input'}),
            'reference': forms.TextInput(attrs={'class': 'form-input'}),
            'recorded_by': forms.Select(attrs={'class': 'form-select'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'role', 'phone', 'joining_date', 'status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['recipient', 'title', 'message', 'notification_type', 'is_read']
        widgets = {
            'recipient': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'notification_type': forms.Select(attrs={'class': 'form-select'}),
            'is_read': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

class TrialBookingForm(forms.ModelForm):
    class Meta:
        model = TrialBooking
        fields = ['first_name', 'last_name', 'email', 'phone', 'program', 'message', 'status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

# ----------------- PUBLIC FORMS ----------------- #

class PublicRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'you@email.com'}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': '+91 00000 00000'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'create a password'}))

class PublicTrialBookingForm(forms.ModelForm):
    class Meta:
        model = TrialBooking
        fields = ['first_name', 'last_name', 'email', 'phone', 'program', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 00000 00000'}),
            'program': forms.Select(attrs={}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your goal...'}),
        }
