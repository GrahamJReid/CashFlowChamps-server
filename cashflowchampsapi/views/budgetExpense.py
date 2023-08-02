from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from cashflowchampsapi.models import BudgetExpense, Expense, Budget

class BudgetExpenseView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            budgetexpense = BudgetExpense.objects.get(pk=pk)
            serializer = BudgetExpenseSerializer(budgetexpense)
            return Response(serializer.data)
        except BudgetExpense.DoesNotExist:
          return Response({'message': 'Cart is empty'}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        budgetexpense = BudgetExpense.objects.all()
        serializer = BudgetExpenseSerializer(budgetexpense, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        expenseId = Expense.objects.get(pk=request.data["expense_id"])
        budgetId = Budget.objects.get(pk=request.data["budget_id"])

        budgetexpense = BudgetExpense.objects.create(
            expenseId = expenseId,
            budget_id =budgetId
        )
        serializer = BudgetExpenseSerializer(budgetexpense)
        return Response(serializer.data)  
    
    def update(self, request, pk):
      
        budgetexpense = BudgetExpense.objects.get(pk=pk)
        budgetexpense.budget_id= Budget.objects.get(pk=request.data["budget_id"])
        budgetexpense.expense_id = Expense.objects.get(pk=request.data["expense_id"])
        
        budgetexpense.save()

    def destroy(self, request, pk):
        budgetexpense = BudgetExpense.objects.get(pk=pk)
        budgetexpense.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class BudgetExpenseSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = BudgetExpense
        fields = ('id', 'budget_id', 'expense_id')

    