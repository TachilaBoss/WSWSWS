# Generated by Django 5.0 on 2023-12-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='/static/shop/image/test.jpg', upload_to=''),
        ),
    ]
