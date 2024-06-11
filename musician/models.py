from django.db import models

# Create your models here.

class Musician(models.Model):
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Bass', 'Bass'),
        ('Violin', 'Violin'),
        ('Flute', 'Flute'),
    ]
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"