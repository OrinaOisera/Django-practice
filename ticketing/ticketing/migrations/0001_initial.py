# Generated by Django 3.2 on 2021-06-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('creates_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]