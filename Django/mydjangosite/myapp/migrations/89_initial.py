from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='m')),
                ('texto', models.CharField(max_length=100)),
                ('descripción', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]