# Generated by Django 3.0.3 on 2022-08-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0006_product_haspropertyselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='selectedPropertyValue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
