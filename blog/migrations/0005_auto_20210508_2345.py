# Generated by Django 3.2 on 2021-05-08 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210429_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated data'),
        ),
    ]
