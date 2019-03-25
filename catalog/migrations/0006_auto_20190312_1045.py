# Generated by Django 2.1.5 on 2019-03-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_house_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Код')),
                ('department_name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('department_notes', models.CharField(max_length=4000, verbose_name='Примечания')),
            ],
            options={
                'db_table': '"inventory"."Departments"',
                'ordering': ['department_id'],
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'managed': False, 'ordering': ['region_id']},
        ),
    ]
