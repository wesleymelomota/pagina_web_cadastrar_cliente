# Generated by Django 3.2.8 on 2021-10-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(choices=[('m', 'masculino'), ('f', 'feminino')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cell', models.IntegerField()),
            ],
        ),
    ]
