# Generated by Django 3.2.18 on 2023-04-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
        ('account', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeuser',
            name='trade_request',
            field=models.ManyToManyField(related_name='trade_request', to='community.Posting'),
        ),
        migrations.AddField(
            model_name='tradeuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
