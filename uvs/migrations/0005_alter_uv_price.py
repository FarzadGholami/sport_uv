# Generated by Django 4.0.6 on 2022-08-01 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uvs', '0004_alter_uv_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uv',
            name='price',
            field=models.IntegerField(),
        ),
    ]
