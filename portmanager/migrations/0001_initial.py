# Generated by Django 2.1.7 on 2019-03-07 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='port',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portmanager.Student'),
        ),
    ]