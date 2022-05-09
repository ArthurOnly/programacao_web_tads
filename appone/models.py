from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    job_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="job")
