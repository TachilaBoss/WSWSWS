# Generated by Django 5.0 on 2023-12-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='static/shop/image/test.jpg', upload_to=''),
        ),
    ]
