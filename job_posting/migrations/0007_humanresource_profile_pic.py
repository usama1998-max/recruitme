# Generated by Django 4.1.3 on 2022-11-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posting', '0006_alter_candidate_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanresource',
            name='profile_pic',
            field=models.ImageField(default='default_img/hr.jpg', upload_to='company_logos'),
        ),
    ]