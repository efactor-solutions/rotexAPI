# Generated by Django 4.1.7 on 2023-05-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0005_alter_category_description_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=16)),
                ('message', models.TextField()),
                ('product', models.ManyToManyField(related_name='product', to='product.product')),
            ],
        ),
    ]
