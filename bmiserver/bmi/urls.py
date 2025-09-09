from django.urls import path
from .views import BMICalculatorView, RegisterView, BMIHistoryView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("bmi/", BMICalculatorView.as_view(), name="bmi_calculator"),
    path("bmi/history/", BMIHistoryView.as_view(), name="bmi_history"),
]
