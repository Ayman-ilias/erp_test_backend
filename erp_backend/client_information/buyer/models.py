# from django.db import models

# class Buyer(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
