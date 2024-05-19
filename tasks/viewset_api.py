from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializer import TaskSerializer

# Create your viewsets here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.complete = not task.complete
        task.save()
        return Response({
            'complete': 'True' if task.complete else 'False'
        }, status=status.HTTP_200_OK)
