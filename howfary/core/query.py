import requests

DIRECTIONS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json?origin={source}&destination={destination}&sensor=false&alternatives=true'

DIRECTIONS_LINK_URL = 'https://maps.google.com/maps?saddr={source}&daddr={destination}'

def compute_howfar(source, destination):
    '''
    Returns the distance between source and destination in the below dict
    representation:

    {
        u'duration': {
                        u'text': u'1 day 7 hours',
                        u'value': 111827
                     },
        u'distance': {
                        u'text': u'2,113 km',
                        u'value': 2113027
                     },
        u'status': u'OK'
    }
    '''
    url = DIRECTIONS_API_URL.format(source=source, destination=destination)
    response = requests.get(url)
    assert response.status_code == 200, 'Not able to retrieve distance between source and destination'
    response = response.json()
    return response['routes'][0]['legs'][0]


if __name__ == '__main__':
    print compute_howfar(source='Delhi', destination='Bangalore')
