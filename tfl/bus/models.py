from django.db import models

from tfl import geo

class BusStop(geo.LocationBase):
	
	tfl_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=300)
	direction = models.CharField(max_length=5,blank=True,null=True)
	letter = models.CharField(max_length=5,blank=True,null=True)

	def __unicode__(self):
		return '%s (%s)' % ( self.name, self.letter )

