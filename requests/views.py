from rest_framework import viewsets, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class IsSupportRep(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'support'

class ServiceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Support reps see all, customers only see their own
        if user.role == 'support':
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
