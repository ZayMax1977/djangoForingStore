# Generated by Django 4.2.5 on 2023-10-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_sent_alter_orderitem_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
