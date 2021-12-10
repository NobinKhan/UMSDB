# Generated by Django 3.2.9 on 2021-12-09 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.PositiveBigIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date time created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date time updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('department_code', models.PositiveBigIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date time created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date time updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date time created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date time updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date time created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date time updated at')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
            ],
        ),
    ]
