# Generated by Django 2.1.7 on 2019-04-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('publication_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('query', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('query_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_items.Query'),
        ),
        migrations.AddField(
            model_name='article',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_items.Feed'),
        ),
    ]
