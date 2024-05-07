from django.db import models

# Create your models here.
class Tag(models.Model):
  name=models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.name

class Category(models.Model):
  name=models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.name
  
class EventOrganiser(models.Model):
  name=models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.name
  

class Event(models.Model):
  name=models.CharField(max_length=100, blank=True, null=True)
  location=models.CharField(max_length=200, blank=True, null=True)
  date_of_event=models.DateTimeField(blank=True, null=True)
  tag = models.ManyToManyField(Tag, blank=True, null=True)
  category = models.ManyToManyField(Category, blank=True, null=True)
  price = models.PositiveIntegerField(blank=True, null=True)
  tickets_left = models.PositiveIntegerField(blank=True, null=True)
  organiser = models.ForeignKey(EventOrganiser, on_delete=models.CASCADE, blank=True, null=True)


  def __str__(self):
    return self.name

