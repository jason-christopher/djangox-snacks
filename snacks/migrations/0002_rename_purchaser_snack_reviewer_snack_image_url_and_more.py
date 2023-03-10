# Generated by Django 4.1.5 on 2023-01-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='purchaser',
            new_name='reviewer',
        ),
        migrations.AddField(
            model_name='snack',
            name='image_url',
            field=models.URLField(default='https://http.cat/404'),
        ),
        migrations.AddField(
            model_name='snack',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='snack',
            name='reference_url',
            field=models.URLField(default='https://http.cat/404'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='snack',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
