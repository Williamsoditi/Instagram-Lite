# Generated by Django 4.0.5 on 2022-06-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0003_delete_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
