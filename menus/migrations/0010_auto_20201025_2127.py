# Generated by Django 3.1.2 on 2020-10-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_auto_20201025_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=1024),
            preserve_default=False,
        ),
    ]
