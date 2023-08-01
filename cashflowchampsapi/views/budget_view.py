"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from cashflowchampsapi.models import User, Budget


class BudgetView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            budget = Budget.objects.get(pk=pk)
            serializer = BudgetSerializer(budget)
            return Response(serializer.data)
        except Budget.DoesNotExist:
          return Response({'message': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        budget = Budget.objects.all()
        serializer = BudgetSerializer(budget, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        rUserId = User.objects.get(pk=request.data["userId"])
        

        budget = Budget.objects.create(
            total=request.data["total"],
            income=request.data["income"],
            user_id = rUserId
            
        )
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)  
    
    def update(self, request, pk):

        budget = Budget.objects.get(pk=pk)
        budget.total = request.data["total"]
        budget.income=request.data["income"]
        budget.user_id= User.objects.get(pk=request.data["userId"])
        
       

        budget.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        budget.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
class BudgetSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Budget
        fields = ('id', 'total', 'income', 'user_id')
        depth = 1
