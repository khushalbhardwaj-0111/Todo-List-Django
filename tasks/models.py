from django.db import models

# Create your models here.

class todo(models.Model):
    TASK_PRIORITY = (
        ('p1', 'priority-1'),
        ('p2', 'priority-2'),
        ('p3', 'priority-3'),
        ('p4', 'priority-4')
    )
    todo_id = models.AutoField(max_length=10, primary_key=True, )
    title = models.CharField(max_length=30)
    complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=TASK_PRIORITY)


    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name
