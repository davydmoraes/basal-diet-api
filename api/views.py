from rest_framework import generics

from .models import Food, User, Meal, MealFood
from .serializers import FoodSerializer, UserSerializer, MealSerializer, MealFoodSerializer


'''class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        user = self.request.query_param.get('user')
        if user is not None:
            queryset = queryset.filter(foodUser=user)
        return queryset'''
    
class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()    

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class MealList(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    
class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
        
class MealFoodList(generics.ListCreateAPIView):
    serializer_class = MealFoodSerializer
    queryset = MealFood.objects.all()
    
class MealFoodDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealFoodSerializer
    queryset = MealFood.objects.all()