# Generated by Django 3.2.3 on 2021-09-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_delete_errorinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=2)),
                ('ID_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Student',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
