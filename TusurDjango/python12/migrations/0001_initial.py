
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # No dependencies for this initial migration.
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                # Primary key for the model
                ('id', models.BigAutoField(
                    auto_created=True, 
                    primary_key=True, 
                    serialize=False, 
                    verbose_name='ID'
                )),
                
                # Name field with max length of 200 characters
                ('name', models.CharField(
                    max_length=200, 
                    verbose_name='First Name'
                )),
                
                # Surname field with max length of 200 characters
                ('surname', models.CharField(
                    max_length=200, 
                    verbose_name='Last Name'
                )),
                
                # Email field with a standard maximum length of 254 characters
                ('email', models.EmailField(
                    max_length=254, 
                    verbose_name='Email Address'
                )),
            ],
        ),
    ]