# Generated by Django 4.1.7 on 2023-10-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0012_alter_teaminvitation_team_alter_teaminvitation_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="receipt",
            name="user",
        ),
        migrations.AddField(
            model_name="teaminvitation",
            name="code",
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
