# Generated by Django 5.0.2 on 2024-02-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_myuser_id_alter_myuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
