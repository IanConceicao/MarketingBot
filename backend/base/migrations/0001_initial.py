# Generated by Django 4.2 on 2023-05-01 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("redirect", models.TextField(blank=True, null=True)),
                ("clickEventCount", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Prompt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("imageUrl", models.ImageField(blank=True, null=True, upload_to="")),
                ("impressionCount", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.TextField(primary_key=True, serialize=False)),
                (
                    "clickEvents",
                    models.ManyToManyField(related_name="+", to="base.action"),
                ),
                (
                    "impressions",
                    models.ManyToManyField(related_name="+", to="base.prompt"),
                ),
                ("prompts", models.ManyToManyField(related_name="+", to="base.prompt")),
            ],
        ),
        migrations.AddField(
            model_name="action",
            name="nextPrompt",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="base.prompt",
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="prompt",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="base.prompt",
            ),
        ),
    ]