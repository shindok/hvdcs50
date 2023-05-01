# Generated by Django 4.2 on 2023-05-01 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('detail', models.CharField(blank=True, max_length=2000, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('goalTime', models.DateTimeField(blank=True, null=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.status')),
            ],
        ),
    ]