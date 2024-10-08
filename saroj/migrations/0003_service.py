# Generated by Django 5.0.6 on 2024-06-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saroj', '0002_alter_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Service Title')),
                ('description', models.TextField(max_length=500, verbose_name='Service Description')),
                ('icon', models.CharField(max_length=100, verbose_name='Service Icon')),
            ],
        ),
    ]
