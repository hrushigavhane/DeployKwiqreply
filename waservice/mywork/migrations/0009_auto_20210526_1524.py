# Generated by Django 3.0.7 on 2021-05-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0008_user_message_unique_msg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_message',
            name='unique_msg_status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
