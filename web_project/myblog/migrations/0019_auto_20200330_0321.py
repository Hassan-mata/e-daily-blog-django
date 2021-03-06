# Generated by Django 3.0.3 on 2020-03-30 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_auto_20200330_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Password1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Password2',
            new_name='password2',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Second_name',
            new_name='second_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Username',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='register',
            name='Gender',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.post'),
        ),
    ]
