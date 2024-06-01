from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food, User, Meal, MealFood
from .serializers import FoodSerializer, UserSerializer, MealSerializer, MealFoodSerializer


################  CRUD OVERVIEW  ################
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create Food': '/api/food/',
        'Food List': '/api/food/',
        'Food Details': '/api/food/<int:pk>/',
        'Update Food': '/api/food/<int:pk>/',
        'Delete Food': '/api/food/<int:pk>/',

        'Create User': '/api/user/',
        'User List': '/api/user/',
        'User Details': '/api/user/<int:pk>/',
        'Update User': '/api/user/<int:pk>/',
        'Delete User': '/api/user/<int:pk>/',

        'Create Meal': '/api/meal/',
        'Meal List': '/api/meal/',
        'Meal Details': '/api/meal/<int:pk>/',
        'Update Meal': '/api/meal/<int:pk>/',
        'Delete Meal': '/api/meal/<int:pk>/',

        'Create MealFood': '/api/meal-food/',
        'MealFood List': '/api/meal-food-list',
    }
    return Response(api_urls)

class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MealFoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        meal_id = self.kwargs['meal_id']
        return Food.objects.filter(mealfood__meal_id=meal_id)

class MealList(generics.ListCreateAPIView):
    serializer_class = MealSerializer

    def get_queryset(self):
        queryset = Meal.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

