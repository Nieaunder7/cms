from django.db import models
from project.models import Project

# Create your models here.
class BaseReport(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    result = models.BooleanField()
    def __str__(self):
        return self.name

class UIReaction(BaseReport):
    match_score = models.DecimalField(max_digits=5, decimal_places=2)
    remote_time = models.DateTimeField()
    match_time = models.DateTimeField()

class ChZapping(BaseReport):
    remote_time = models.DateTimeField()
    first_stop_time = models.DateTimeField()
    second_stop_time = models.DateTimeField()
    edge_time = models.DateTimeField()

class ImageMatch(BaseReport):
    match_score = models.DecimalField(max_digits=5, decimal_places=2)
