from .models import Notification

def admin_context(request):
    if request.user.is_authenticated and request.user.is_superuser:
        unread_notifications = Notification.objects.filter(recipient=request.user, is_read=False).count()
        return {
            'unread_notifications_count': unread_notifications,
        }
    return {}
