# Generated by Django 2.2.9 on 2021-09-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vendor_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
