# Generated by Django 2.2.11 on 2020-03-25 20:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20200324_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wiki.Register'),
        ),
        migrations.AlterField(
            model_name='row',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wiki.Register'),
        ),
        migrations.AlterField(
            model_name='wikientry',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
