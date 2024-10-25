from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_user'
    )

    message = models.TextField()

    date = models.DateField()
    time = models.TimeField()

    seen = models.BooleanField(default=False)
