# Generated by Django 3.0.5 on 2020-05-07 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes', '0002_auto_20200506_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_code', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('quotes', models.CharField(max_length=250)),
                ('catgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quotes.Catagory')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Postion',
        ),
    ]
