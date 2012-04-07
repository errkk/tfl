from django.core.management.base import BaseCommand, CommandError

from tfl.bus.models import BusStop
from tfl.bus.api import get_busstop_locations


# import logging
# logger = logging.getLogger('planner')

class Command(BaseCommand):
	help = 'Get busstop locations from TFL and save them in the DB'

	
	def handle(self, *args, **options):

		count = 0
		saved = 0

		for i in get_busstop_locations():
			stop = BusStop()
			stop.lat = float(i['lat'])
			stop.lng = float(i['lng'])
			stop.tfl_id = int(i['id'])
			stop.name = i['name']
			stop.letter = i['letter']
			stop.direction = i['direction']

			count += 1
			if stop.save():
				saved += 1


