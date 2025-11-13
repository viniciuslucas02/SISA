
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('faculdade', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('turno', models.CharField(max_length=20)),
                ('emitido', models.DateField()),
            ],
        ),
    ]
