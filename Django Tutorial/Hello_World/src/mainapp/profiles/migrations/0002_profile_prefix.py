# Generated by Django 3.2.6 on 2021-08-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Dr', 'Dr'), ('Princess', 'Princess'), ('Rev', 'Rev'), ('Prince', 'Prince'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
