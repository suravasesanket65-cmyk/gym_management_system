from decimal import Decimal
from django.db.models import Sum, F, Count
from django.utils import timezone
from core.models import (
    Member, Trainer, Payment, Attendance, Subscription,
    Appointment, Expense, InventoryItem, MembershipPlan, TrialBooking
)
from datetime import timedelta

class DashboardService:
    @staticmethod
    def get_kpis():
        today = timezone.localdate()
        this_month_start = today.replace(day=1)
        next_7_days = today + timedelta(days=7)

        total_members = Member.objects.count()
        active_members = Member.objects.filter(status='Active').count()
        total_trainers = Trainer.objects.count()

        revenue_agg = Payment.objects.filter(payment_status='Completed').aggregate(Sum('amount'))
        total_revenue = revenue_agg['amount__sum'] or Decimal('0.00')

        today_attendance = Attendance.objects.filter(check_in_time__date=today).count()

        expiring_memberships = Subscription.objects.filter(
            end_date__gte=today,
            end_date__lte=next_7_days,
            status='Active'
        ).count()

        pending_agg = Payment.objects.filter(payment_status='Pending').aggregate(Sum('amount'))
        pending_payments = pending_agg['amount__sum'] or Decimal('0.00')

        upcoming_appointments = Appointment.objects.filter(
            appointment_date__gte=today,
            status='Scheduled'
        ).count()

        expense_agg = Expense.objects.filter(expense_date__gte=this_month_start).aggregate(Sum('amount'))
        total_expenses = expense_agg['amount__sum'] or Decimal('0.00')

        net_profit = total_revenue - total_expenses
        low_stock_items = InventoryItem.objects.filter(quantity__lte=F('min_stock_level')).count()
        total_trial_bookings = TrialBooking.objects.count()

        return {
            'total_members': total_members,
            'active_members': active_members,
            'total_trainers': total_trainers,
            'total_revenue': total_revenue,
            'today_attendance': today_attendance,
            'expiring_memberships': expiring_memberships,
            'pending_payments': pending_payments,
            'upcoming_appointments': upcoming_appointments,
            'total_expenses': total_expenses,
            'net_profit': net_profit,
            'low_stock_items': low_stock_items,
            'total_trial_bookings': total_trial_bookings,
        }

    @staticmethod
    def get_recent_members():
        return Member.objects.order_by('-joined_date', '-id')[:5]

    @staticmethod
    def get_upcoming_appointments_table():
        today = timezone.localdate()
        return Appointment.objects.select_related('member', 'trainer').filter(
            appointment_date__gte=today,
            status='Scheduled'
        ).order_by('appointment_date', 'start_time')[:5]

    @staticmethod
    def get_revenue_attendance_chart():
        today = timezone.localdate()
        months = []
        revenue_data = []
        attendance_data = []

        for i in range(5, -1, -1):
            month_date = (today.replace(day=1) - timedelta(days=28 * i)).replace(day=1)
            months.append(month_date.strftime('%b'))

            if month_date.month == 12:
                next_month = month_date.replace(year=month_date.year + 1, month=1)
            else:
                next_month = month_date.replace(month=month_date.month + 1)

            rev_agg = Payment.objects.filter(
                payment_status='Completed',
                transaction_date__gte=month_date,
                transaction_date__lt=next_month
            ).aggregate(Sum('amount'))
            revenue_data.append(float(rev_agg['amount__sum'] or Decimal('0.00')))

            att_count = Attendance.objects.filter(
                check_in_time__gte=month_date,
                check_in_time__lt=next_month
            ).count()
            attendance_data.append(att_count)

        return {
            'labels': months,
            'revenue_data': revenue_data,
            'attendance_data': attendance_data
        }

    @staticmethod
    def get_membership_distribution():
        distribution = Subscription.objects.filter(status='Active').values('plan__plan_name').annotate(count=Count('id'))
        labels = [d['plan__plan_name'] for d in distribution]
        data = [d['count'] for d in distribution]
        
        if not labels:
            labels = ['No Plans']
            data = [1]
            
        return {
            'labels': labels,
            'data': data
        }
