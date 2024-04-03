# Generated by Django 5.0.3 on 2024-04-03 19:08

import django.db.models.deletion
import user.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('block', models.IntegerField(blank=True, null=True)),
                ('office', models.IntegerField(blank=True, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=500)),
                ('account_pic', models.ImageField(blank=True, default='_user/defaults/default_account.png', null=True, upload_to='_user/host_profile_pics')),
                ('host_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('username', models.CharField(default='d_username', max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('profile_pic', models.ImageField(blank=True, default='_user/defaults/default_profile.png', null=True, upload_to='_user/user_profile_pics')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='superuser')),
                ('is_staff', models.BooleanField(default=True, verbose_name='superuser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('following', models.ManyToManyField(blank=True, to='user.host')),
                ('hosts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hosts', to='user.host')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user.manager.UserManager()),
            ],
        ),
    ]
