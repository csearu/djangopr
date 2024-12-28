from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
    monthly_expenses = models.IntegerField(default=0)
    monthly_income = models.IntegerField(default=0)


class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='uploads/')
    formatted_image = models.ImageField(upload_to='formatted_uploads/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title