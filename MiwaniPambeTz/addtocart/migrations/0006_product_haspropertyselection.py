# Generated by Django 3.0.3 on 2022-08-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0005_auto_20220813_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hasPropertySelection',
            field=models.BooleanField(default=False),
        ),
    ]
