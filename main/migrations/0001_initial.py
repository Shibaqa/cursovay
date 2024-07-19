# Generated by Django 5.0.7 on 2024-07-18 10:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mailing_time', models.DateTimeField(auto_now=True, verbose_name='время последней рассылки')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='статус попытки')),
                ('response', models.CharField(blank=True, max_length=200, null=True, verbose_name='ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'log',
                'verbose_name_plural': 'logs',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='тема')),
                ('content', models.TextField(verbose_name='содержание')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало')),
                ('next_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='следующее')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='конец')),
                ('interval', models.CharField(choices=[('once_a_day', 'ежедневно'), ('once_a_week', 'раз в неделю'), ('once_a_month', 'раз в месяц')], default='разовая', max_length=50, verbose_name='интервал')),
                ('status', models.CharField(choices=[('start', 'start'), ('finish', 'finish'), ('created', 'created')], max_length=50, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='действующая')),
                ('client', models.ManyToManyField(to='main.client', verbose_name='кому')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ('start_date',),
                'permissions': [('set_is_activated', 'Может отключать рассылку')],
            },
        ),
    ]
