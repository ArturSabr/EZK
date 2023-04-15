# Generated by Django 4.2 on 2023-04-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_applicationmodel_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcursModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('image', models.ImageField(upload_to='news/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Конкурс',
                'verbose_name_plural': 'Конкурсы',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('image', models.ImageField(upload_to='news/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Коментарий'),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='contact_mam',
            field=models.CharField(max_length=123, verbose_name='Контакты матери'),
        ),
    ]