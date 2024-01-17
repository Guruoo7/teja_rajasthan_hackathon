from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'  # Specify the collection name in MongoDB
        app_label = 'mainapp'  # Replace 'your_app_name' with the actual name of your Django app
