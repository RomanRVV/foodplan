# Generated by Django 4.2.5 on 2023-09-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='classic',
            field=models.BooleanField(default=False, verbose_name='классик'),
        ),
        migrations.AddField(
            model_name='order',
            name='keto',
            field=models.BooleanField(default=False, verbose_name='кето'),
        ),
        migrations.AddField(
            model_name='order',
            name='lowcarb',
            field=models.BooleanField(default=False, verbose_name='низкоуглеводная'),
        ),
        migrations.AddField(
            model_name='order',
            name='vegan',
            field=models.BooleanField(default=False, verbose_name='вегетарианская'),
        ),
        migrations.AddField(
            model_name='product',
            name='classic',
            field=models.BooleanField(default=False, verbose_name='классик'),
        ),
        migrations.AddField(
            model_name='product',
            name='keto',
            field=models.BooleanField(default=False, verbose_name='кето'),
        ),
        migrations.AddField(
            model_name='product',
            name='lowcarb',
            field=models.BooleanField(default=False, verbose_name='низкоуглеводная'),
        ),
        migrations.AddField(
            model_name='product',
            name='vegan',
            field=models.BooleanField(default=False, verbose_name='вегетарианская'),
        ),
    ]
