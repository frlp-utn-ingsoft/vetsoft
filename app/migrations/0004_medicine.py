from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('dose', models.IntField),
            ],
        ),
    ]
