#get_distance.py
import googlemaps
from datetime import datetime
import config

gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

now = datetime.now()

"""
distance_matrix(
client, origins, destinations, mode=None, language=None,
avoid=None, units=None, departure_time=None,
arrival_time=None, transit_mode=None,
transit_routing_preference=None, traffic_model=None)
"""

def distance(
	start_loc, end_loc, mode='transit',avoid=None,
	units='imperial', depart=now, arrive=now, transit_mode='bus',
	transit_pref='less walking', traffic='best guess'
):
	# FIXME: Need to validate start and end_loc somehow

	# Specify either depart or arrive
	if depart:
		arrive = None
	else:
		depart = None

	# only specify transit_mode/transit_pref if mode == trafic
	if mode.lower() != 'transit':
		transit_mode = None
		transit_pref = None
	elif not (mode.lower() == 'driving' and depart != None):
		traffic = None


	distance_result = gmaps.distance_matrix(
		start_loc, end_loc, mode=mode, units=units,
		departure_time=depart, arrival_time=arrive,
		transit_mode=transit_mode,
		transit_routing_preference=transit_pref,
		traffic_model=traffic, avoid=avoid
	)

	return distance_result

if __name__ == "__main__":
	print 'Not implemented yet'
