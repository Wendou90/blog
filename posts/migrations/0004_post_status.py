# Generated by Django 4.1.2 on 2022-10-09 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221009_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.status'),
        ),
    ]
