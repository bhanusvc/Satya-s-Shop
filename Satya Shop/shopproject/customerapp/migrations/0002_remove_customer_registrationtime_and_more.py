# Generated by Django 5.0.7 on 2024-07-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='registrationtime',
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferences',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
