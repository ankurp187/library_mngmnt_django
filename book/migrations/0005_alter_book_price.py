# Generated by Django 5.0.6 on 2024-06-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_assignment_assigned_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]