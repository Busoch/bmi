from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BMISerializer, RegisterSerializer, BMIRecordSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import BMIRecord

class BMICalculatorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BMISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        weight = serializer.validated_data["weight"]      # kg
        height_cm = serializer.validated_data["height"]   # cm
        height_m = height_cm / 100.0

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        record = BMIRecord.objects.create(
            user=request.user,
            weight=weight,
            height=height_cm,
            bmi=round(bmi, 2),
            category=category,
        )

        return Response({"bmi": round(bmi, 2), "category": category})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    
class BMIHistoryView(generics.ListAPIView):
    serializer_class = BMIRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BMIRecord.objects.filter(user=self.request.user).order_by("-created_at")