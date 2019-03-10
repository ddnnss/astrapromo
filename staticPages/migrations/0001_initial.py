# Generated by Django 2.1.7 on 2019-03-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='showCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseName', models.CharField(max_length=255, verbose_name='Заголовок кейса')),
                ('caseNameSlug', models.CharField(blank=True, max_length=255, verbose_name='Заголовок кейса')),
                ('siteUrl', models.CharField(max_length=255, verbose_name='Адрес сайта')),
                ('image', models.ImageField(upload_to='showcases/', verbose_name='Картинка')),
                ('showcaseInfo', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('showInHomePage', models.BooleanField(default=False, verbose_name='Отображать на главной')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный кейс?')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]
