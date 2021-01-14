# Generated by Django 3.1.4 on 2021-01-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('todo_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]