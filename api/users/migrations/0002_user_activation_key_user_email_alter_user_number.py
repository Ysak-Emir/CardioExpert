# Generated by Django 4.2 on 2023-04-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(max_length=25, null=True, unique=True, verbose_name='Номер врача'),
        ),
    ]