# Generated by Django 4.2.2 on 2023-06-15 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("showtimeplan", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Etudiants",
            new_name="User",
        ),
        migrations.AlterModelTable(
            name="user",
            table="etudiants",
        ),
    ]
