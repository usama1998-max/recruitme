# Generated by Django 4.1.3 on 2022-11-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posting', '0007_humanresource_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanresource',
            name='profile_pic',
            field=models.ImageField(default='default_img/hr.jpg', upload_to='hr_profile_pic'),
        ),
    ]