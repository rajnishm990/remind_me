from rest_framework import viewsets, status , mixins
from rest_framework.response import Response 
from rest_framework.decorators import action 
from django.shortcuts import get_object_or_404 
from .models import Reminder 
from .serializers import ReminderSerializer 
import logging
logger = logging.getLogger(__name__)

class ReminderViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Reminder.objects.all().order_by('-reminder_date','-reminder_time')
    serializer_class =ReminderSerializer 

    def create(self,request,*args , **kwargs):
        logger.info(f"Creating new reminder with data: {request.data}")
        serializer = ReminderSerializer(data= request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "status": "success",
                    "message": "Reminder created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        
        logger.warning(f"Invalid reminder data: {serializer.errors}")
        return Response(
            {
                "status": "error",
                "message": "Failed to create reminder",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancel a pending reminder."""
        reminder = get_object_or_404(Reminder, pk=pk)
        
        if reminder.status != 'pending':
            return Response(
                {"status": "error", "message": f"Cannot cancel reminder with status '{reminder.status}'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        reminder.status = 'cancelled'
        reminder.save()
        
        return Response(
            {"status": "success", "message": "Reminder cancelled successfully"},
            status=status.HTTP_200_OK
        )



    
    
