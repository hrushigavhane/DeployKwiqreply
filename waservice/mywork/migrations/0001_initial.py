# Generated by Django 3.0.7 on 2021-05-14 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sandbox_Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sandbox Names For Clients',
            },
        ),
        migrations.CreateModel(
            name='template_master',
            fields=[
                ('temp_id', models.AutoField(primary_key=True, serialize=False)),
                ('namespace', models.CharField(max_length=30)),
                ('temp_name', models.CharField(max_length=50)),
                ('temp_payload', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('username', models.EmailField(max_length=254)),
                ('comp_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('user_img', models.ImageField(upload_to='pics')),
                ('sent_message', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Registered Users',
            },
        ),
        migrations.CreateModel(
            name='user_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wa_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('m_type', models.CharField(max_length=12)),
                ('m_url', models.CharField(blank=True, max_length=1000)),
                ('m_service', models.CharField(blank=True, max_length=15)),
                ('m_fileName', models.CharField(blank=True, max_length=100)),
                ('m_from', models.CharField(max_length=15)),
                ('m_status', models.CharField(blank=True, max_length=10)),
                ('m_media', models.TextField(blank=True)),
                ('m_previous', models.CharField(blank=True, max_length=5)),
                ('m_current', models.CharField(blank=True, max_length=5)),
                ('m_session', models.CharField(default='', max_length=8)),
                ('timestamp1', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'User Mesages',
            },
        ),
        migrations.CreateModel(
            name='Submit_Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=1000)),
                ('product', models.CharField(max_length=100)),
                ('business_impact', models.CharField(max_length=100)),
                ('ticketdate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywork.User_Details')),
            ],
            options={
                'verbose_name_plural': 'Ticket Form Submission Data',
            },
        ),
        migrations.CreateModel(
            name='Sandbox_Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webhook', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywork.User_Details')),
            ],
            options={
                'verbose_name_plural': 'Sandbox Client Webook URL',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comp_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywork.User_Details')),
            ],
            options={
                'verbose_name_plural': 'Sales Form Submission Data',
            },
        ),
        migrations.CreateModel(
            name='Business_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comp_name', models.CharField(default='Company name', max_length=40)),
                ('Business_desc', models.CharField(default='Default description', max_length=200)),
                ('Business_Category', models.CharField(default='Others', max_length=40)),
                ('facebook_id', models.CharField(default='Facebook id', max_length=40)),
                ('business_disp_name', models.CharField(default='disp name', max_length=40)),
                ('about_business', models.CharField(default='About', max_length=200)),
                ('business_address', models.CharField(default='Company address', max_length=200)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_number', models.CharField(default=91123456879, max_length=14)),
                ('radio', models.CharField(default='yes', max_length=3)),
                ('website', models.CharField(default='website', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywork.User_Details')),
            ],
            options={
                'verbose_name_plural': 'Business Profile Form Submission Data',
            },
        ),
    ]
