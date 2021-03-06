# Generated by Django 2.1.5 on 2019-03-13 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190312_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Код')),
                ('employee_firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('employee_lastname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('employee_middlename', models.CharField(max_length=255, verbose_name='Отчество')),
                ('employee_email', models.CharField(max_length=255, verbose_name='email')),
                ('employee_phone_work', models.CharField(max_length=255, verbose_name='тел.')),
                ('employee_note', models.CharField(max_length=255, verbose_name='Примечание')),
                ('employee_full_fio', models.CharField(max_length=255, verbose_name='ФИО польностью')),
                ('employee_is_chief', models.IntegerField(default=0, verbose_name='Руководитель')),
                ('employee_is_respons', models.IntegerField(default=0, verbose_name='МО лицо')),
                ('employee_office_id', models.ForeignKey(db_column='employee_office_id', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Office', verbose_name='Офис')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Код')),
                ('position_name', models.CharField(max_length=255, verbose_name='Должность')),
                ('position_notes', models.CharField(max_length=255, verbose_name='Примечание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'managed': False, 'ordering': ['department_region_id', 'department_id']},
        ),
        migrations.AddField(
            model_name='position',
            name='position_department_id',
            field=models.ForeignKey(db_column='position_department_id', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Department', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='employees',
            name='employee_position_id',
            field=models.ForeignKey(db_column='employee_position_id', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Position', verbose_name='Должность'),
        ),
    ]
