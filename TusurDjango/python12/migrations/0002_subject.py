from django.db import migrations, models


class Migration(migrations.Migration):

    # This migration depends on the initial migration of the 'django_primer' app
    dependencies = [
        ('django_primer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                # The primary key for the 'Subject' model
                ('id', models.BigAutoField(
                    auto_created=True, 
                    primary_key=True, 
                    serialize=False, 
                    verbose_name='ID'
                )),

                # The name field for the subject with a maximum length of 20 characters
                ('name', models.CharField(
                    max_length=20, 
                    verbose_name='Subject Name'
                )),
            ],
        ),
    ]