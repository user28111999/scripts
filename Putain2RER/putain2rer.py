from twilio.rest import Client
import android
import time
import json

droid = android.Android()

with open('api.json') as f:
	data = json.load(f)

auth_token = data[sid]
auth_token = data[token]
client = Client(account_sid, auth_token)

droid.startLocating()
event = droid.eventWaitFor('location', 10000)

# CENSORED
homeLat = 666
homeLng = 666
workLat = 666
workLng = 666

while True:
	try:
		provider = event.result['data']['gps']['provider']
		if provider == 'gps':
			lat = str(event['data']['gps']['latitude'])
			lng = str(event['data']['gps']['longitude'])
			latlng = 'lat: ' + lat + ' lng: ' + lng
			if lat == homeLat & lng == homeLng:
				call = client.calls.create(
					url = 'CENSORED',
					to = 'CENSORED',
					from_ = 'CENSORED'
				)
				break
			if lat == workLat & lng == workLng:
				call = client.calls.create(
					url = 'CENSORED',
					to = 'CENSORED',
					from_ = 'CENSORED'
				)
				break
			continue
		else: 
			continue
	except KeyError:
		continue
