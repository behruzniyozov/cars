from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MediaFile(models.Model):
    file = models.FileField(upload_to='media/')
    car= models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='media_files', null=True, blank=True)

    def __str__(self):
        return self.file.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)
   

    def __str__(self):
        return f"Message from {self.name}"
