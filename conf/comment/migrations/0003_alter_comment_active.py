# Generated by Django 4.0.3 on 2022-03-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_rename_post_comment_product_alter_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
