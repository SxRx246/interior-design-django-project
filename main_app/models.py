from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class Designer(models.Model):
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     years_of_experience = models.IntegerField()
    
#     class Meta:
#         db_table = 'designers'
        
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        DESIGNER = "designer", "Designer"
        CUSTOMER = "customer", "Customer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
        # null=True
    )
    
    class Meta:
        db_table = 'users'
    
    
class Project(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField(null=False)
    description = models.TextField(null = True)
    pictures = models.ImageField(upload_to='projects-pictures/', null=True)
    designer = models.ForeignKey(User, on_delete=models.CASCADE , related_name='projects')
    # category = models.CharField()
    
    class Meta:
        db_table = 'projects'
    
    def __str__(self):
        return self.name