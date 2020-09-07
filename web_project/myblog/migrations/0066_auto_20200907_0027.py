# Generated by Django 3.0.5 on 2020-09-06 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0065_auto_20200907_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.post'),
        ),
    ]