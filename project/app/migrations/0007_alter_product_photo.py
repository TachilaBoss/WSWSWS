# Generated by Django 5.0 on 2023-12-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='/test.jpg', upload_to=''),
        ),
    ]
