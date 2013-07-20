import requests

URL = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins={source}&destinations={destination}&sensor=false'

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
    url = URL.format(source=source, destination=destination)
    response = requests.get(url)
    assert response.status_code == 200, 'Not able to retrieve distance between source and destination'
    response = response.json()
    return response['rows'][0]['elements'][0]


if __name__ == '__main__':
    print compute_howfar(source='Delhi', destination='Bangalore')
