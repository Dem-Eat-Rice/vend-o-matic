from operator import inv
from unicodedata import name
from django.http import JsonResponse
from .models import Inventory, VendingMachine, Beverage
from .serializers import VendingMachineSerializer, BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Used for the '' url pathway
# Below function adds and dispenses coins from the vending machine
@api_view(['PUT', 'DELETE'])
def coin_function(request):
    vendingmachine = VendingMachine.objects.get(name='GoodYear Tire Lobby')
    if request.method == 'PUT':
        if request.data['coin'] == 1:
            vendingmachine.add_coin(request.data['coin'])
            vendingmachine.save()
            return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': request.data['coin']})
    elif request.method == 'DELETE':
        coins_to_dispense = vendingmachine.return_coin()
        vendingmachine.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': coins_to_dispense})


# Used for the 'inventory/' url pathway
# Below function checks the stock of all beverages in the inventory
@api_view(['GET'])
def inventory_count(request):
    # request.path returns '/inventory/', so below we change it to 'inventory'
    path = request.path[1:len(request.path)-1]
    inventory = Inventory.objects.get(name=path)
    remaining_beverages = inventory.get_inventory_count()
    """
    Omitting the below. Would use if we didn't assume that the vending machine 
        would start off fully stocked.
    """
    # inventory.soda_count = Beverage.objects.filter(name="SODA").count()
    # inventory.water_count = Beverage.objects.filter(name="WATER").count()
    # inventory.juice_count = Beverage.objects.filter(name="JUICE").count()
    # inventory.save()
    return Response(remaining_beverages, status=status.HTTP_200_OK)


# Used for inventory/<int:id>/' url pathway
# This is where we check individual item stock via GET request or purchase an item via PUT request
@api_view(['GET', 'PUT'])
def select_and_purchase(request, id):
    beverage = Beverage.objects.get(id=id)
    inventory = Inventory.objects.get(name=beverage.inventory_name)
    vendingmachine = VendingMachine.objects.get(name=inventory.machine_name)
    specific_beverage_count = Beverage.objects.filter(name=beverage).count()
    
    if request.method == 'GET':
        return Response(specific_beverage_count, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        if beverage.id:
            # Check that we have at least 2 coins to vend an item
            if vendingmachine.coin > 1:
                    inventory.item_vended(beverage.name)
                    vendingmachine.item_vended()
                    vendingmachine.save()
                    inventory.save()
                    beverage.delete()
                    return Response(status=status.HTTP_200_OK, headers={'X-Coins': vendingmachine.item_vended(), 'X-Inventory-Remaining': inventory.get_item_count(beverage.name)})
                
            return Response(status=status.HTTP_403_FORBIDDEN, headers={'X-Coins': vendingmachine.return_coin()})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, headers={'X-Coins':vendingmachine.coin})

        
