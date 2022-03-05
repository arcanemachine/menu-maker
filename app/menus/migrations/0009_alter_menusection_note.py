# Generated by Django 3.2 on 2022-03-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0008_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusection',
            name='note',
            field=models.CharField(blank=True, help_text="An optional note about this section (e.g.'Drinks come with complimentary refills.')", max_length=256, null=True),
        ),
    ]
