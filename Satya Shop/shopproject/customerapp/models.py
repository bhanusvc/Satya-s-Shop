from django.db import models

# Create your models here.
class Customer(models.Model):
    # Initial registration fields
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    gender = models.CharField(blank=False, choices=gender_choices, max_length=1)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False)

    # Profile completion fields
    date_of_birth = models.DateField(blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "customerreg_table"
