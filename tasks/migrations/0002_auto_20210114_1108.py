# Generated by Django 3.1.4 on 2021-01-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]