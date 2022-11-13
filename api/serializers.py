from rest_framework import serializers
from habits.models import Habit, DateRecord, User

class HabitSerializer(serializers.ModelSerializer):
    date_records=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Habit
        fields = ['pk', 'name', 'goal', 'user', 'created_at', 'unit', 'planstart', 'journal', 'date_records',]


class UserSerializer(serializers.ModelSerializer):
    habits=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['pk', 'username', 'habits',]

class DateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateRecord
        fields = ['pk', 'habit', 'actual', 'date',]        

class CreateHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'goal', 'unit', 'planstart', 'journal',]