from django.core.management.base import BaseCommand, CommandError

from tfl.bike.models import BikeStation
from tfl.bike.api import get_boris_data


# import logging
# logger = logging.getLogger('planner')

class Command(BaseCommand):
	help = 'Get Bike Station locations from TFL and save them in the DB'

	
	def handle(self, *args, **options):

		count = 0
		saved = 0

		for i in get_boris_data():
			print i

			s = BikeStation()
			s.lat = i['lat']
			s.lng = i['lng']
			s.tfl_id = i['id']
			s.name = i['name']			

			count += 1
			if s.save():
				saved += 1

		print 'Saved: %d out of %d' % ( saved, count )
