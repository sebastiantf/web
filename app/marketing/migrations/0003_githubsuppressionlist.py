# Generated by Django 2.1.7 on 2019-04-29 23:05

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20190212_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubSuppressionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('query', models.EmailField(max_length=255)),
                ('comments', models.TextField(blank=True, max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
