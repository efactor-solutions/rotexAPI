# Generated by Django 4.1.7 on 2023-05-11 20:36

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to=page.models.upload_to)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
