from django.db import models


# Create your models here.
class Photographers(models.Model):
    name = models.CharField(max_length=50,blank=False)
    studio = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class Appointments(models.Model):
    pname = models.ForeignKey(Photographers, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


# p = Photographers(name='John Doe', studio='Doe Studios', email = "reyes@gmail.com", phone = "1234567890", address = "123 Main St, Anytown, USA")