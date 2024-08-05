from rest_framework import serializers
from medicals.models import login_details,signup_details,medicine_details

class medicalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine_details
        fields = '__all__'