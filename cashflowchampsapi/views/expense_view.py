"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from cashflowchampsapi.models import User, Expense


class ExpenseView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            expense = Expense.objects.get(pk=pk)
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data)
        except Expense.DoesNotExist:
          return Response({'message': 'Expense does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        expense = Expense.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        rUserId = User.objects.get(pk=request.data["userId"])

        expense = Expense.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            price=request.data["price"],
            user_id = rUserId
            
        )
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)  
    
    def update(self, request, pk):

        expense = Expense.objects.get(pk=pk)
        expense.title = request.data["title"]
        expense.description=request.data["description"]
        expense.price=request.data["price"]
        expense.user_id= User.objects.get(pk=request.data["userId"])
        
       

        expense.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
class ExpenseSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Expense
        fields = ('id', 'title', 'description','price', 'user_id')
        depth = 1
