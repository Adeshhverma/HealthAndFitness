# Generated by Django 4.0.3 on 2022-04-12 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0011_expert_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(default=django.utils.timezone.now, verbose_name='start date')),
                ('to_date', models.DateField(default=django.utils.timezone.now, verbose_name='End date')),
                ('expert_user_name', models.CharField(default='abc', max_length=45)),
                ('request_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='not confirm', max_length=45)),
                ('response_text', models.CharField(default='no response', max_length=45)),
                ('user_message_text', models.CharField(default=' ', max_length=45)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='healthapp.patient')),
            ],
        ),
    ]
