# Generated by Django 5.0.3 on 2024-03-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Score', models.IntegerField()),
                ('Birthdate', models.DateTimeField(auto_now_add=True)),
                ('Grade', models.CharField(max_length=10)),
            ],
        ),
    ]
