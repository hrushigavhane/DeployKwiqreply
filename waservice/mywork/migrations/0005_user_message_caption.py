# Generated by Django 3.0.7 on 2021-05-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0004_auto_20210521_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_message',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
