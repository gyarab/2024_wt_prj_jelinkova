# Generated by Django 5.1.7 on 2025-03-28 10:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_diet_productdiet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdiet',
            name='diet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.diet'),
        ),
        migrations.AlterField(
            model_name='productdiet',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
