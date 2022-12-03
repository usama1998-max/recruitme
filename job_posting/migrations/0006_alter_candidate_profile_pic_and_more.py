# Generated by Django 4.1.3 on 2022-11-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posting', '0005_alter_humanresource_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profile_pic',
            field=models.ImageField(default='hr.jpg', upload_to='candidate_profile'),
        ),
        migrations.AlterField(
            model_name='humanresource',
            name='company_logo',
            field=models.ImageField(default='hr.jpg', upload_to='company_logos'),
        ),
    ]
