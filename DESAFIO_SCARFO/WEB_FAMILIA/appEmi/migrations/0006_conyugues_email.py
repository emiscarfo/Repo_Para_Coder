# Generated by Django 4.1.3 on 2022-11-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmi', '0005_conyugues'),
    ]

    operations = [
        migrations.AddField(
            model_name='conyugues',
            name='email',
            field=models.EmailField(default=2001, max_length=254),
            preserve_default=False,
        ),
    ]
