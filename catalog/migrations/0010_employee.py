# Generated by Django 2.1.5 on 2019-03-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20190314_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Код')),
                ('employee_lastname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('employee_firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('employee_middlename', models.CharField(max_length=255, verbose_name='Отчество')),
                ('employee_email', models.CharField(max_length=255, verbose_name='email')),
                ('employee_phone_work', models.CharField(max_length=255, verbose_name='тел.')),
                ('employee_note', models.CharField(max_length=255, verbose_name='Примечание')),
                ('employee_full_fio', models.CharField(max_length=255, verbose_name='ФИО польностью')),
                ('employee_is_chief', models.IntegerField(default=0, verbose_name='Руководитель')),
                ('employee_is_respons', models.IntegerField(default=0, verbose_name='МО лицо')),
            ],
            options={
                'db_table': '"inventory"."Employees"',
                'ordering': ['employee_id'],
                'managed': False,
            },
        ),
    ]
