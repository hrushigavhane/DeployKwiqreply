# Generated by Django 3.0.7 on 2021-05-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0014_user_message_user_message_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_profile',
            name='ip_address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
