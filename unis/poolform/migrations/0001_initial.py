# Generated by Django 2.2.7 on 2019-11-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=200)),
                ('endereco', models.TextField(max_length=200)),
                ('altura', models.TextField(max_length=5)),
                ('peso', models.TextField(max_length=5)),
                ('imc', models.TextField(max_length=15)),
            ],
        ),
    ]