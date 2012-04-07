from django.db import models

from tfl import geo

class BikeStation(geo.LocationBase):
	
	tfl_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=300)
	docks = models.IntegerField(null=True,blank=True)

	def __unicode__(self):
		return self.name

