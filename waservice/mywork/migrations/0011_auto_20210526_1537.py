# Generated by Django 3.0.7 on 2021-05-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0010_auto_20210526_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_message',
            name='timestamp1',
            field=models.DateTimeField(blank=True),
        ),
    ]
