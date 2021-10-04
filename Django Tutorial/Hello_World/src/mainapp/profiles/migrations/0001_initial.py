# Generated by Django 3.2.6 on 2021-09-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(choices=[('Rev', 'Rev'), ('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Prince', 'Prince'), ('Dr', 'Dr'), ('Princess', 'Princess'), ('Ms', 'Ms')], max_length=15)),
                ('first_name', models.CharField(default='', max_length=60)),
                ('last_name', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default='', max_length=60)),
            ],
        ),
    ]
