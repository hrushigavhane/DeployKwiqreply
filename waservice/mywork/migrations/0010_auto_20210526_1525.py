# Generated by Django 3.0.7 on 2021-05-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0009_auto_20210526_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_message',
            name='unique_msg_status',
            field=models.CharField(blank=True, default='sent', max_length=10),
        ),
    ]