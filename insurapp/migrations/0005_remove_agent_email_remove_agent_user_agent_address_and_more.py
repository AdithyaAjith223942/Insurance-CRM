# Generated by Django 5.1.1 on 2024-12-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurapp', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='user',
        ),
        migrations.AddField(
            model_name='agent',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='agent_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='agents/'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
