from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    CATEGORY_CHOICES = [
        ('Strength', 'Strength'),
        ('Conditioning', 'Conditioning'),
        ('Combat', 'Combat'),
        ('Recovery', 'Recovery'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    full_name = models.CharField(max_length=100)
    role_specialty = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    linkedin_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class TrialBooking(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Converted', 'Converted'),
        ('Cancelled', 'Cancelled'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, related_name='trial_bookings')
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"


class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Suspended', 'Suspended'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.plan_name


class Subscription(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Cancelled', 'Cancelled'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.member} - {self.plan.plan_name}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Net Banking', 'Net Banking'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='payments')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.amount} - {self.payment_status}"


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='attendances')
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.member} - {self.check_in_time}"


class ClassSchedule(models.Model):
    DAY_OF_WEEK_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='schedules')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='schedules')
    class_name = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_capacity = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.class_name} - {self.day_of_week}"



class Exercise(models.Model):
    name = models.CharField(max_length=150)
    target_muscle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    equipment = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=50, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Inactive', 'Inactive'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='workout_plans')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='workout_plans')
    name = models.CharField(max_length=150)
    goal = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.member}"

class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    sets = models.PositiveIntegerField()
    repetitions = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True, help_text="Duration in seconds")
    rest_time = models.PositiveIntegerField(blank=True, null=True, help_text="Rest time in seconds")
    order = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.exercise.name} for {self.workout_plan.name}"

class DietPlan(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Inactive', 'Inactive'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='diet_plans')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='diet_plans')
    name = models.CharField(max_length=150)
    goal = models.CharField(max_length=150)
    daily_calories = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.member}"

class DietMeal(models.Model):
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='meals')
    meal_type = models.CharField(max_length=100)
    meal_time = models.TimeField(blank=True, null=True)
    food_description = models.TextField()
    calories = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    protein = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fats = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.meal_type} - {self.diet_plan.name}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('No Show', 'No Show'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='appointments')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    appointment_date = models.DateField(db_index=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    appointment_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['trainer', 'appointment_date']),
        ]

    def __str__(self):
        return f"{self.appointment_type} - {self.member} with {self.trainer}"

class InventoryItem(models.Model):
    STATUS_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Low Stock', 'Low Stock'),
        ('Out of Stock', 'Out of Stock'),
    ]

    item_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, db_index=True)
    sku = models.CharField(max_length=100, unique=True, db_index=True)
    quantity = models.PositiveIntegerField(default=0)
    min_stock_level = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='In Stock', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sku})"

class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(db_index=True)
    description = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses_recorded')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"

class Staff(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    joining_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=150)
    message = models.TextField()
    notification_type = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['recipient', 'is_read']),
        ]

    def __str__(self):
        return f"To {self.recipient.username}: {self.title}"
