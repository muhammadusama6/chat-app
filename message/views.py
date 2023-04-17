from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from message.models import Message
from message.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # def create(self, request, *args, **kwargs):
    #     if request.data['sender'] == '' or not request.data['sender']:
    #         # request.data['sender'] = request.user
    #         data = request.data.copy()
    #         data['sender'] = request.user.id
    #     serializer = self.serializer_class(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(data=serializer.data)

    def perform_create(self, serializer):
        sender_id = self.request.user.id
        sender = User.objects.get(id=sender_id)
        serializer.save(sender=sender)

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.sender == self.request.user:
            self.perform_destroy(instance)
            return Response({"message": "Message deleted."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You don't have permission to delete this message."},
                            status=status.HTTP_403_FORBIDDEN)
