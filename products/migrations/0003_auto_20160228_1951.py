# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
    ]