# Generated by Django 5.0.4 on 2024-04-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abs', '0009_alter_account_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='photo',
            field=models.ImageField(default='None', upload_to='upload/product', verbose_name='Фото'),
        ),
    ]
