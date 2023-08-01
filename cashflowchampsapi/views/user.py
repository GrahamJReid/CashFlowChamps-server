"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cashflowchampsapi.models import User

class UserView(ViewSet):
    """Rare Users view"""
    
    def list(self, request):
        """Handle GET requests to get all users
        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
      try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
      except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        user.username = request.data["username"]
        user.email=request.data["email"]
        user.uid = request.data["uid"]
        
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = User
        fields = ('id', 'username','email', 'uid')
        depth = 1
