from django.db import models

# Create your models here.


class Designer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    years_of_experience = models.IntegerField()
    
    class Meta:
        db_table = 'designers'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Project(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField(null = True)
    pictures = models.ImageField(upload_to='projects-pictures/', null=True)
    designer = models.ForeignKey(Designer , on_delete=models.CASCADE , related_name='projects')
    # category = models.CharField()
    
    class Meta:
        db_table = 'projects'
    
    def __str__(self):
        return self.name