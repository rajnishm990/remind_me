from rest_framework  import serializers
from django.utils import timezone 
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder 
        fields = ['id', 'title', 'message', 'reminder_date', 'reminder_time',
            'notification_method', 'recipient', 'status', 'created_at']
    
    def validate(self,data):
        reminder_data = data.get('reminder_date')
        reminder_time = data.get('reminder_time')
        
        if reminder_data and reminder_time :
            reminder_datetime = timezone.make_aware(timezone.datetime.combine(reminder_data, reminder_time))
        
            if reminder_datetime <= timezone.now():
                raise serializers.ValidationError("Reminder datetime must be in the future.")
        
        #notification validation 
        notification_method = data.get('notification_method')
        recipient = data.get('recipient')

        if notification_method == 'email':
            # Simple email validation
            if not recipient or '@' not in recipient:
                raise serializers.ValidationError({
                    "recipient": "A valid email address is required for email notifications."
                })
        elif notification_method == 'sms':
            # Simple phone number validation
            if not recipient or not recipient.replace('+', '').isdigit():
                raise serializers.ValidationError({
                    "recipient": "A valid phone number is required for SMS notifications."
                })
        
        return data