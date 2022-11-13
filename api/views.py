from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

from habits.models import User, DateRecord, Habit
from .serializers import HabitSerializer, CreateHabitSerializer


# Create your views here.
class HabitListView(APIView):
    
    def get(self,request, format=None):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
 

class HabitDetailView(RetrieveUpdateDestroyAPIView):
    queryset         = Habit.objects.filter()
    serializer_class = HabitSerializer

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class HabitCreateView (CreateAPIView):
    serializer_class = CreateHabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




