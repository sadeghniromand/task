# Generated by Django 4.0.3 on 2022-03-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='product name')),
                ('description', models.TextField(verbose_name='product description')),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
