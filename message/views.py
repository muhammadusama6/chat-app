from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.response import Response

from message.models import Message
from message.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        sender_id = self.request.user.id
        sender = User.objects.get(id=sender_id)
        serializer.save(sender_name=sender)

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender_name=user) | Message.objects.filter(receiver_name=user)

    def destroy(self, request, *args, **kwargs):
        """
        Override delete method to allow only the sender to delete the message.
        """
        instance = self.get_object()
        if instance.sender_name == self.request.user:
            self.perform_destroy(instance)
            return Response({"message": "Message deleted."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You don't have permission to delete this message."}, status=status.HTTP_403_FORBIDDEN)
