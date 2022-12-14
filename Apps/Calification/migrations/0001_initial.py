# Generated by Django 4.1.1 on 2022-10-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('califications', models.SmallIntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Store.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.user')),
            ],
        ),
    ]
