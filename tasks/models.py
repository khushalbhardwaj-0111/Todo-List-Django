from django.db import models
import datetime

# Create your models here.

class todo(models.Model):
    todo_id = models.AutoField(max_length=10, primary_key=True)
    title = models.CharField(max_length=30, null=False)
    complete = models.BooleanField(default=False)
    priority = models.ForeignKey(to=priority, on_delete=models.CASCADE)


    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name


# ? should I do this as follows or incorporate that to the todo model itself as choice[char-field]
class priority(models.Model):
  TASK_PRIORITY = [
        ('p1', 'Red'),
        ('p2', 'Orange'),
        ('p3', 'Blue'),
        ('p4', 'White')
  ]
  priority = models.CharField(max_length=10, blank=True, choices=TASK_PRIORITY)

class dueDate(models.Model):
  current_time = datetime.datetime.now() 
  today = current_time.today().date()
  tomorrrow = datetime.date.today() + datetime.timedelta(days=1)

  # * TODO: Complete this model configuration and make migrations and migrate the datebase
  # ? Should I put due dates to the task
  
