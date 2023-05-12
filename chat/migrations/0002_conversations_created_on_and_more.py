# Generated by Django 4.1.7 on 2023-05-11 16:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_category_description_alter_product_description'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversations',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='conversations',
            name='product',
        ),
        migrations.AddField(
            model_name='conversations',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
            preserve_default=False,
        ),
    ]
