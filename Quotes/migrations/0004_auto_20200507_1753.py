# Generated by Django 3.0.5 on 2020-05-07 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes', '0003_auto_20200507_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='catgory',
            new_name='catagory',
        ),
    ]
