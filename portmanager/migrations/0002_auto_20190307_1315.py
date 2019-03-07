# Generated by Django 2.1.7 on 2019-03-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortAllocation',
            fields=[
                ('port_number', models.IntegerField(primary_key=True, serialize=False)),
                ('student', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='port',
            name='student',
        ),
        migrations.DeleteModel(
            name='Port',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
