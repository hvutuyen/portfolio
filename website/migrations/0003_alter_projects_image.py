# Generated by Django 4.0.4 on 2022-05-04 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='my_projects'),
        ),
    ]
