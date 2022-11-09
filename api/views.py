from rest_framework.views import APIView
from rest_framework.views import Response

from habits.models import User, DateRecord, Habit
from .serializers import HabitSerializer


# Create your views here.
class HabitListView(APIView):
    def get(self, request,format=None):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer
        return Response(serializer.data) 
 



