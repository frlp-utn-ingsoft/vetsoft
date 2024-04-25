from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('dose', models.IntegerField()),
            ],  
        )
    ]