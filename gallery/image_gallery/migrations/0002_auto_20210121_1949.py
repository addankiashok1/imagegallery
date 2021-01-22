# Generated by Django 2.2 on 2021-01-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]