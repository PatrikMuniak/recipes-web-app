# Generated by Django 2.2.3 on 2019-08-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receip_name', models.CharField(max_length=70)),
                ('ingredients', models.CharField(max_length=255)),
            ],
        ),
    ]
