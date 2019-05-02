# Generated by Django 2.0.2 on 2019-05-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/blog')),
            ],
        ),
    ]
