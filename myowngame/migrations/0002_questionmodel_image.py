# Generated by Django 4.1.5 on 2023-01-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myowngame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images'),
        ),
    ]
