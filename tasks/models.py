from django.db import models
import datetime

# Create your models here.

class todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title
