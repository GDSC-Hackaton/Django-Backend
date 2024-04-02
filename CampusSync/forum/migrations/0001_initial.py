# Generated by Django 5.0.3 on 2024-04-02 15:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
                ('asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_question_asker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_questions', to='forum.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('answered_by_host', models.BooleanField(default=False)),
                ('answering_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answering_host', to='user.host')),
                ('answering_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answering_user', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_of_answer', to='forum.question')),
            ],
        ),
        migrations.CreateModel(
            name='EventForum',
            fields=[
                ('forum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forum.forum')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            bases=('forum.forum',),
        ),
    ]
