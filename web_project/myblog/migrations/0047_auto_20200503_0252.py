# Generated by Django 3.0.5 on 2020-05-03 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0046_auto_20200503_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='sub_title',
            new_name='headline',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.post'),
        ),
    ]