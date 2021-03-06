# Generated by Django 2.2.4 on 2019-08-31 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import records.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecordTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_record_title', models.CharField(max_length=30, verbose_name='レコードタイトル')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_record_image', models.ImageField(blank=True, default='records/default.jpg', upload_to=records.models.get_file_path, verbose_name='写真')),
                ('user_record_content', models.CharField(max_length=300, verbose_name='内容')),
                ('user_record_elapsed_time', models.DurationField(verbose_name='経過時間')),
                ('user_record_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='記録時間')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_record_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.UserRecordTitle')),
            ],
        ),
        migrations.CreateModel(
            name='GroupRecordTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_record_title', models.CharField(max_length=30, verbose_name='練習メニュー')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupRecordContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_record_image', models.ImageField(blank=True, default='records/default', upload_to=records.models.get_file_path)),
                ('group_record_content', models.CharField(max_length=300, verbose_name='練習記録')),
                ('group_record_elapsed_time', models.DateTimeField(verbose_name='経過時間')),
                ('group_record_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='記録時間')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
                ('group_record_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.GroupRecordTitle')),
            ],
        ),
    ]
