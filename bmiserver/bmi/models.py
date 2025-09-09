from django.db import models
from django.contrib.auth.models import User

class BMIRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bmi_records")
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.bmi} ({self.category})"
