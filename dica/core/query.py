import requests

URL = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins={source}&destinations={destination}&sensor=false'

def compute_howfar(source, destination):
    url = URL.format(source=source, destination=destination)
    response = requests.get(url)
    assert response.status_code == 200, 'Not able to retrieve distance between source and destination'
    response = response.json()
    distance_attributes = response['rows'][0]['elements'][0]
    distance = distance_attributes['distance']['text']
    duration = distance_attributes['duration']['text']
    return (distance, duration)


if __name__ == '__main__':
    print compute_howfar(source='Delhi', destination='Bangalore')
