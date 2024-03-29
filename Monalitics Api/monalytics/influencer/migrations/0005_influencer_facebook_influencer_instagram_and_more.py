# Generated by Django 5.0.1 on 2024-02-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0004_alter_influencer_compaigns'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='facebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='instagram',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='linkedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='snapchat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='tiktok',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='twitter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='influencer',
            name='youtube',
            field=models.BooleanField(default=False),
        ),
    ]
