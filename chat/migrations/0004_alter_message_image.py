# Generated by Django 5.0 on 2024-01-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
