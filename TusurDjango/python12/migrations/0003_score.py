
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    # The migration depends on the second migration of the 'django_primer' app.
    dependencies = [
        ('django_primer', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                # Primary key for the Score model
                ('id', models.BigAutoField(
                    auto_created=True, 
                    primary_key=True, 
                    serialize=False, 
                    verbose_name='ID'
                )),

                # The value field for the score, holding a float number
                ('value', models.FloatField(
                    verbose_name='Score Value'
                )),

                # Foreign key to the Student model, with cascade deletion
                ('student', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, 
                    to='django_primer.Student', 
                    verbose_name='Student'
                )),

                # Foreign key to the Subject model, with cascade deletion
                ('subject', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, 
                    to='django_primer.Subject', 
                    verbose_name='Subject'
                )),
            ],
        ),
    ]

