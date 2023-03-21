# Generated by Django 4.1.7 on 2023-03-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('likes', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default=None, max_length=1)),
            ],
        ),
    ]
