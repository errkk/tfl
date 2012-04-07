from django.db import models
from math import cos, radians, sin, sqrt, atan2

 
def cosrad(n):
    "Return the cosine of ``n`` degrees in radians."
    return cos(radians(n))
 
def haversine((lat1, long1), (lat2, long2)):
    """Calculate the distance between two points on earth.
    """
    earth_radius = 6371  # km
    dLat = radians(lat2 - lat1)
    dLong = radians(long2 - long1)
 
    a = (sin(dLat / 2) ** 2 +
         cosrad(lat1) * cosrad(lat2) * sin(dLong / 2) ** 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = earth_radius * c
    print d
    return d
 
def distance(a, b):
    "Return the distance between two points that have .lat and .lng members."
    return haversine(
        (float(a.lat), float(a.lng)),
        (float(b.lat), float(b.lng)))


def calculate_minmax_radius(lat, lng, radius, use_km = True):        
    if use_km:
        radius = radius * 0.621371192;

    degradius = radius / 69

    lng_min = lng - radius / abs(cos(radians(lat)) * 69)
    lng_max = lng + radius / abs(cos(radians(lat)) * 69)
    lat_min = lat - degradius
    lat_max = lat + degradius
    return lng_min, lng_max, lat_min, lat_max



class LocationBase(models.Model):
    '''
    Abstract base class for locational models
    '''
    class Meta:
        abstract = True
        
    lng = models.FloatField(null = True, blank = True)
    lat = models.FloatField(null = True, blank = True)

    @classmethod
    def items_in_radius(cls, lat, lng, radius = 0.5, use_km = True):
        # Find Bounding Box
        lng_min, lng_max, lat_min, lat_max = calculate_minmax_radius(lat, lng, radius, use_km)
        # Query DB
        results = cls.objects.filter(lng__range=(lng_min, lng_max), lat__range=(lat_min, lat_max))
        # Sort by distance
        return sorted(results, key=lambda o: int( haversine( ( lat,lng ),(o.lat,o.lng) ) ) )








