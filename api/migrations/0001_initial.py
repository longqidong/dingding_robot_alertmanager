# Generated by Django 2.1.8 on 2019-08-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alertname', models.CharField(max_length=100)),
                ('instance', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=30)),
                ('startsAt', models.DateTimeField()),
                ('endsAt', models.DateTimeField()),
                ('receiver', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('post_times', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'alert',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=30)),
                ('receiver_num', models.IntegerField()),
                ('dingtalk_robot_api', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'receiver',
            },
        ),
        migrations.AlterUniqueTogether(
            name='receiver',
            unique_together={('receiver', 'receiver_num')},
        ),
    ]