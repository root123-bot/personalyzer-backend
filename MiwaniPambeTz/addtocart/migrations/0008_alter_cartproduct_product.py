# Generated by Django 3.2 on 2022-08-22 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0007_cartproduct_selectedpropertyvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addtocart.product'),
        ),
    ]
