# Generated by Django 4.2.7 on 2023-11-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillapp', '0003_skill_created_at_skill_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='proficiency',
            field=models.CharField(default='L', max_length=2, verbose_name=[('H', 'High', 'M', 'Medium', 'L', 'Low')]),
        ),
    ]