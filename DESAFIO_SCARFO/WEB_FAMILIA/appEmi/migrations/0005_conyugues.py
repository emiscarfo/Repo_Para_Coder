# Generated by Django 4.1.3 on 2022-11-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmi', '0004_remove_familiar_email_remove_familiar_fecha_nac_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conyugues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_de_pariente', models.CharField(max_length=25)),
            ],
        ),
    ]
