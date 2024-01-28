from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food, User, Meal, MealFood
from .serializers import FoodSerializer, UserSerializer, MealSerializer, MealFoodSerializer


################  CRUD OVERVIEW  ################
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create Food':'/api/create-food/',
        'Food List':'/api/food-list',
        'Food Details':'/api/food-detail/<int:pk>',
        'Update Food':'/api/update-food/<int:pk>',
        'Delete Food':'/api/delete-food/<int:pk>',   

        'Create User':'/api/create-user/',
        'User List':'/api/user-list',
        'User Details':'/api/user-detail/<int:pk>',
        'Update User':'/api/update-user/<int:pk>',
        'Delete User':'/api/delete-user/<int:pk>',
        
        'Create Meal':'/api/create-meal/',
        'Meal List':'/api/meal-list',
        'Meal Details':'/api/meal-detail/<int:pk>',
        'Update Meal':'/api/update-meal/<int:pk>',
        'Delete Meal':'/api/delete-meal/<int:pk>',
        
        'Create MealFood':'/api/create-meal-food/',
        'MealFood List':'/api/meal-food-list',
        
    }
    return Response(api_urls)



################  FOOD CRUD  ################
@api_view(['POST'])
def createFood(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)

@api_view(['GET'])
def foodList(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def foodDetail(request, pk):
    food = Food.objects.get(id=pk)
    serializer = FoodSerializer(food, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteFood(request, pk):
    food = Food.objects.get(id=pk)
    food.delete()
                
    return Response('Item successfully deleted')

@api_view(['POST'])
def updateFood(request, pk):
    food = Food.objects.get(id=pk)
    serializer = FoodSerializer(instance=food, data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)



################  USER CRUD  ################
@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)

@api_view(['GET'])
def userList(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
                
    return Response('Item successfully deleted')




################  MEAL CRUD  ################
@api_view(['POST'])
def createMeal(request):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)

@api_view(['GET'])
def mealList(request):
    meal = Meal.objects.all()
    serializer = MealSerializer(meal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mealDetail(request, pk):
    meal = Meal.objects.get(id=pk)
    serializer = MealSerializer(meal, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def updateMeal(request, pk):
    meal = Meal.objects.get(id=pk)
    serializer = MealSerializer(instance=meal, data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMeal(request, pk):
    meal = Meal.objects.get(id=pk)
    meal.delete()
                
    return Response('Item successfully deleted')




################  MEAL-FOOD  ################
@api_view(['GET'])
def mealFoodList(request):
    mealFood = MealFood.objects.all()
    serializer = MealFoodSerializer(mealFood, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createMealFood(request):
    serializer = MealFoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
                
    return Response(serializer.data)
