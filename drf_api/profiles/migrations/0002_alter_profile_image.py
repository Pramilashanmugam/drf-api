# Generated by Django 3.2.25 on 2024-09-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dwqek0e9x/image/upload/v1726177562/earth-3537401_640_cbeub3.jpg', upload_to='images/'),
        ),
    ]
